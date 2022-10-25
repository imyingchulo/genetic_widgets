import click
from genetic_widgets.genetic_widgets import GeneticWidgets

@click.group()
def main():
    pass

# @click.command()
# def test():
#     print("hello world")

@click.command()
@click.option( '--sample_list', metavar='<str>', required=True, help='full path to random draw sample list' )
@click.option( '--output_dir', metavar='<str>', required=True, help='output file directory')
@click.option( '--output_name', metavar='<str>', required=True, help='output file name' )
@click.option( '--exclude_samples', metavar='<str>', help='optional argument. exclude sample list' )
@click.option( '--random_draw_nb', metavar='<int>', required=True, help='random draw number, interger require' )
def random_draw_samples( self, sample_list, output_dir, output_name, exclude_samples,random_draw_nb):
    GeneticWidgets.random_draw_samples(self=self, sample_list=sample_list, output_dir=output_dir,
                                       output_name=output_name,exclude_samples=exclude_samples,
                                       random_draw_nb=random_draw_nb)

@click.command()
@click.option( '--arr1', metavar='<str>', required=True, help='full path to sample list a' )
@click.option( '--arr2', metavar='<str>', required=True, help='full path to smaple list b')
def find_intersection( self, arr1, arr2):
    GeneticWidgets.find_intersection(self=self, arr1=arr1, arr2=arr2)

@click.command()
@click.option( '--sample_list', metavar='<str>', required=True, help='full path to sample list. List should only contain id and no header' )
@click.option( '--pheno_data', metavar='<str>', required=True, help='full path to pheon type data, with header "id" and "pheno"')
@click.option( '--output_dir', metavar='<str>', required=True, help='output file directory' )
@click.option( '--output_name', metavar='<str>', required=True, help='output file name')
def subset_phenotype_data( self, sample_list, pheno_data, output_dir, output_name):
    GeneticWidgets.subset_phenotype_data(self=self, sample_list=sample_list, pheno_data=pheno_data,
                                         output_dir=output_dir, output_name=output_name)

@click.command()
@click.option( '--input_file', metavar='<str>', required=True, help='full path to bim file')
@click.option( '--output_file', metavar='<str>', required=True, help='full path to output file [output_dir]/[new_output.bim]')
@click.option( '--snp_id_index', metavar='<int>', required=True, help='index of snpid in .bim' )
@click.option( '--chr_index', metavar='<int>', required=True, help='index of chr in .bim')
@click.option( '--pos_index', metavar='<int>', required=True, help='index of pos in .bim' )
@click.option( '--a1_index', metavar='<int>', required=True, help='index of a1 in .bim')
@click.option( '--a2_index', metavar='<int>', required=True, help='index of a2 in .bim')
def make_uniq_marker( self, input_file, output_file, snp_id_index, chr_index, pos_index, a1_index, a2_index):
    GeneticWidgets.make_uniq_marker(self=self, snp_id_index=snp_id_index, input_file=input_file,
                                    chr_index=chr_index, pos_index=pos_index, a1_index=a1_index,
                                    a2_index=a2_index, output_file=output_file)

@click.command()
@click.option( '--invr', metavar='<str>', required=True, help='full path to invr file')
@click.option( '--summary_data', metavar='<str>', required=True, help='full path to summaru statistics data')
@click.option( '--output_dir', metavar='<int>', required=True, help='output dir' )
@click.option( '--outputname', metavar='<int>', required=True, help='output file name')
@click.option( '--snp_id_index', metavar='<int>', required=True, help='index of id in GWAS summaty file' )
@click.option( '--pos_index', metavar='<int>', required=True, help='index of pos in GWAS summaty file')
@click.option( '--a1_index', metavar='<int>', required=True, help='index of a1 in GWAS summaty file')
@click.option( '--a2_index', metavar='<int>', required=True, help='index of a2 in in GWAS summaty file')
def updatae_gwas_summary( self, invr, summary_data, output_dir, outputname, snp_id_index, pos_index, a1_index, a2_index):
    GeneticWidgets.updatae_gwas_summary(self=self, invr=invr, summary_data=summary_data, output_dir=output_dir,
                                        outputname=outputname, snp_id_index=snp_id_index,
                                        pos_index=pos_index, a1_index=a1_index, a2_index=a2_index)

main.add_command( random_draw_samples )
main.add_command( find_intersection )
main.add_command( subset_phenotype_data )
main.add_command( make_uniq_marker )
main.add_command( updatae_gwas_summary )
