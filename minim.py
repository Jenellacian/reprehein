# Filtering df_cmts where PosterID is in df_inf's PosterID
df_cmts = df_cmts.loc[df_cmts['PosterID'].isin(df_inf['PosterID'])]

print("\nFiltered df_cmts:")
print(df_cmts)
