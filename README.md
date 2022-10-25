# Tools for genetic analysis - Genetic Widgets
---

This package is for preparing the input data(GWAS summary statistics, random draw sample to subset vcf and update GWAS summary statistics with liftover information file) to build PS/PRS model.


:octocat: Functions include in the package:

1. random draw samples
2. find_intersection
3. subset phenotype data
4. make uniq id in GWAS summary statistics 
5. updatae gwas summary (lifted gwas summary)

## Environment setup

1. Setup virtualenv

```shell
$ python3 -m venv venv
```

2. Activate virtualenv

```shell
$ source ./venv/bin/activate
```

3. Install this package

```shell
$ pip install -e .
```

## Usage guidance

###  Subset vcf files with random draw individuals 
Make sure the sample id in individuals list is independent and uniq.
Users can use `exclude_samples` to exclude individuals from individuals list.

`find intersection` is a function to find the overlap between two lists

###  Subset pheno type data
subset the phenotype data with individual list

###  Make uniq marker
This function transform the rsid into `chr:pos:a1:a2`

###  Update GWAS summary statistics ( update the GWAs with lifted and inverted nucleotide)
This function is using the output file generate by triple liftover package: https://github.com/GraceSheng/triple-liftOver




