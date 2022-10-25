import random
import os
import csv
from collections import defaultdict

class GeneticWidgets(object):
    def random_draw_samples(self, sample_list, output_dir, output_name, exclude_samples, random_draw_nb):

        def random_draw(slist):
            with open("{}/{}.txt".format(output_dir, output_name), 'w') as fin:
                random_sample = random.sample(slist, random_draw_nb)
                rs = '\n'.join(random_sample)
                fin.write(rs)
        print("random sample list created {}.txt".format(output_name))

        dict_sample={}
        slist=[]
        with open("{}".format(sample_list), 'r') as fin:
            lines = fin.readlines()
            for line in lines:
                slist.append(line.strip())
                key = "{}".format(line.strip())
                dict_sample[key] = 1

        if os.path.exists("{}".format(exclude_samples)):
            with open("{}".format(exclude_samples), 'r') as fin:
                for id in fin:
                    if id in dict_sample:
                        dict_sample[id] = int(dict_sample[id]) + 1
            # update list
            new_list=[]
            for key, value in dict_sample.items():
                if value == 1:
                    new_list.append(key)
                else:
                    pass
            slist=new_list
            random_draw(slist)
        else:
            random_draw(slist)

    def find_intersection(self, arr1, arr2):
        # Use a breakpoint in the code line below to debug your script.
        return set(arr1).intersection(arr2)


    def subset_phenotype_data(self, sample_list, pheno_data, output_dir, output_name):
        header = ""
        sscore_table = {}
        with open(pheno_data) as sin:
            for index, rows in enumerate(sin.readlines()):
                row = rows.split()
                if index == 0:
                    header = "{}\t{}\n".format(row[0], row[1])
                else:
                    key = "{}".format(row[0])
                    sscore_table[key] = "{}\t{}\n".format(row[0], row[1])

        with open(sample_list) as indvin:
            with open("{}/{}".format(output_dir,output_name), 'w') as fout:
                fout.write(header)
                for row in indvin:
                    key = row.strip()
                    if key in sscore_table:
                        fout.write(sscore_table[key])

        with open("{}/{}.log".format(output_dir, output_name), 'w') as login:
            login.write("pheno:{}\nindv:{}\noutput:{}/{}\n".format(pheno_data, sample_list, output_dir, output_name))


    def make_uniq_marker(self, input_file, snp_id_index, chr_index, pos_index, a1_index, a2_index, output_file):
        rows = []
        with open("{}".format(input_file)) as file:
            filebim = csv.reader(file, delimiter='\t')
            for line in filebim:
                # if line[1] == ".":
                # line[1] = "{}:{}:{}:{}".format(line[0],line[3],line[4],line[5])
                line[snp_id_index] = "chr{}:{}:{}:{}".format(line[chr_index], line[pos_index], line[a1_index], line[a2_index])
                rows.append(line)

        with open(output_file, 'w') as fout:
            csv_writer = csv.writer(fout, delimiter='\t')
            csv_writer.writerows(rows)

    def updatae_gwas_summary(self, invr, summary_data, output_dir, outputname, snp_id_index, pos_index, a1_index, a2_index):
        def convert(allele):
            if allele == 'C':
                return 'G'
            elif allele == 'G':
                return 'C'
            elif allele == 'A':
                return 'T'
            elif allele == 'T':
                return 'A'
            else:
                print('Exception')

        table = defaultdict()
        output = []
        # extract the info from summary statistics
        with open("{}".format(summary_data)) as fin:
            for index, row in enumerate(fin.readlines()):
                summary = row.split()
                if index == 0:
                    output.append(summary)
                else:
                    key = "{}".format(summary[snp_id_index])
                    table[key] = summary

        final_summary = []
        common_snp = set()
        with open("{}".format(invr)) as fin:
            next(fin)  # skip the first line
            for index, row in enumerate(fin.readlines()):
                data = row.split()
                key = "{}".format(data[0])
                if data[4] == "lifted" and key in table:
                    table[key][pos_index] = data[2]
                    output.append(table[key])
                    common_snp.add(key)
                elif data[4] == "inverted" and key in table:
                    table[key][a1_index] = convert(table[key][a1_index])
                    table[key][a2_index] = convert(table[key][a2_index])
                    output.append(table[key])
                    common_snp.add(key)

        drop_snps = []
        for key in table:
            if key not in common_snp:
                drop_snps.append(key)

        final_summary = "\n".join(map(str, output))
        final_summary = final_summary.replace('[', '').replace(']', '').replace('\'', '').replace(',', '').replace(' ','\t')

        drop_snps = "\n".join(map(str, drop_snps))

        with open("{}/{}.txt".format(output_dir, outputname), 'w') as fout:
            fout.write(final_summary)

        with open("{}/{}_dropSNPs.txt".format(output_dir, outputname), 'w') as fout:
            fout.write(drop_snps)


