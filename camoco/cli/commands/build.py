import camoco as co
from camoco.Tools import DummyRefGen

def build_cob(args):
    # Build the refgen
    if not args.ignore_refgen_membership:
        refgen = co.RefGen(args.refgen)
    else:
        refgen = DummyRefGen() 
    # Basically just pass all the CLI arguments to the COB class method  
    co.COB.from_table(
        args.filename,
        args.name,
        args.description,
        refgen,
        # Optional arguments
        rawtype=args.rawtype,
        quantile=False,
        max_gene_missing_data=args.max_gene_missing_data,
        max_accession_missing_data=args.max_accession_missing_data,
        min_single_sample_expr=args.min_single_sample_expr,
        min_expr=args.min_expr,
        max_val=args.max_val,
        dry_run=args.dry_run,
        quality_control=args.skip_quality_control
    )
    print("Build successful!")

def build_refgen(args):
    co.RefGen.from_gff(
        args.filename, 
        args.name,
        args.description,
        args.build,
        args.organism,
        # Optional Arguments
        chrom_feature=args.chrom_feature,
        gene_feature=args.gene_feature,
        ID_attr=args.ID_attr,
        attr_split=args.attr_split
    )
    print("Build successful!")
