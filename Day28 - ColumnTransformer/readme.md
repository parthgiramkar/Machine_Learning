With Column_Transformer , we can apply changes to the desired columns all at a once  

Syntax - tuples inside the transfomers list with the syntax - Tuple format	('name', transformer, columns)


ct = ColumnTransformer(
    transformers=[
        ('name1', transformer1, columns_for_transformer1),
         ('name2', transformer2, columns_for_transformer2),
        # you can add more
    ],
    remainder='drop'/'passthrough'
