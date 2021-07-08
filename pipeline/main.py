import time

import pandas as pd
from pipeline.pipeline_lib.clean_feature.clean_data import CleanData
from pipeline.pipeline_lib.read_data_and_prepare_to_clean.prepare_cols import Prepare
from pipeline.pipeline_lib.read_data_and_prepare_to_clean.stabilize_dfs import StabilizeDF
from pipeline.pipeline_value.value_read_dfs import path, origin_dict
from store_dfs_lib.controller_store_dfs import ControllerStoreDFs
from dir.origin_dir import OriginDir
from pipeline.pipeline_value.value_for_clean_data import severity_illness_dict
from store_dfs_lib.store_dfs import StoreDF

pd.set_option('mode.chained_assignment', None)

#  ---- Downland Data  ----
origin_dir = OriginDir(path, "origin29.03.2021")
# kaggle = Ka
# .+936*ggleUI(origin_dict, origin_dir.path)
# kaggle.downland_data()
# origin_dir.unzip_file()

#  ---- Read the Data  ----
# dfs, dfs_names = ReadDfs.read(origin_dir)

dfs = []
dfs_names = []

for var in origin_dict:
    origin_dict[var].append("")  # make sheet_name=origin_dict[var][2] == "" if not origin_dict[var][2]
    dfs_names.append(var)
    vars()[var] = origin_dir.read_file_as_DataFrame(name_file=origin_dict[var][1],
                                                    sheet_name=origin_dict[var][2])
    dfs.append(vars()[var])

dfs_store = ControllerStoreDFs(StoreDF(dfs, dfs_names))

#  ---- DS consolidation ----
stabilize = StabilizeDF(dfs_store)
stabilize.stabilize_DFs()
canada = dfs_store.get_df_by_name("canada")
del stabilize

# ---- Rename & Del Unnecessary Columns ----
Prepare.organize_cols(dfs_store)





# ---- Shape of Data ----
# store_df.print_shape_dfs()
# dfs_store.print_cols_by_df()
# dfs_store.print_cols_values_by_dfs()

#  ---- Clean ----
CleanData.clean_data(dfs_store)


# ---- Age -----
# for df in [world, canada]:
#     df["age_band"] = df["age"]
#     Cage.clean_age_col(df, "age",  ["Not Reported"])
#
# # age from birth_year
# for df in [france, indonesia]:
#     df["confirmed_date_year"] = df["confirmed_date"].apply(lambda x: x.year)
#     df["age"] = df["confirmed_date_year"] - df["birth_year"]
#
# # kerla
# kerla["age"] = kerla["age"].astype("str")
# Clean.replace_value_by_comparison(kerla, "age", {np.nan: ["Unspecified", "51F", "nan"]})
#
# # format to float
# for dataset in [india_wiki, india_data, guatemala, philippines, singapore, mexico, colombia,
#                 vietnam, kerla, hong_kong, world, canada]:
#     dataset["age"] = dataset["age"].astype("float")
#
# track.print_col_values_by_dfs('age')
#
#
# # ---- Age Band ----
# # canada
# Clean.replace_value_by_comparison(canada, "age_band", {"1": ["<10", "<1"]})
#
# # "20 - 29 Years" => "20-29"
# Clean.replace_value_by_comparison(usa, "age_band", {np.nan: ["Unknown"]})
# usa.age_band = usa.age_band.apply(lambda x: Clean.clean_str_replace(x, [" ", "Years"], "") if x == x else x)
#
# #  "10s" -> "10"
# Clean.replace_value_by_comparison(japan, "age_band", {np.nan: ["investigating", "Checking"],
#                                                       "0s": ["Under 10", "Under teens"]})
# for df in [korea, japan]:
#     df.age_band = df.age_band.apply(lambda x: int(Clean.clean_str_replace(x, ["s"], "")) if x == x else x)
#
#
# for dataset in [france, tunisia, indonesia, guatemala, singapore, philippines, india_data,
#                 india_wiki, vietnam, colombia, mexico, france, kerla, hong_kong]:
#     dataset["age_band"] = dataset["age"][dataset["age"].notnull()].apply(lambda x: int((x // 10) * 10))
#
#
# # age_band from dirty age (range and more)
# for df in [world, canada, toronto, usa]:
#     Cage.to_age_band(df, "age_band", ["Not Reported", "19 and younger", "nan"])
#
# track.print_col_values_by_dfs('age_band')
#
#
# # ----Country ----
# # Complete country by dataset
# country_df_names = track.dfs_names.copy()
# country_df_names.remove("world")
#
# for df_name in country_df_names:
#     name = df_name.replace("_", " ")
#     name = df_name.replace("data", " ")
#     name = df_name.replace("wiki", " ")
#     store_dfs_lib.get_df_by_name(df_name)["country"] = name
#
# world["country"] = world["country"].apply(lambda x: x.lower() if x == x else np.nan)
# track.print_col_values_by_dfs('country')
#
# # ---- Region ----
# india_wiki["region"] = "karnataka"
# kerla["region"] = "kerla"
# toronto["region"] = "toronto"
# hong_kong["region"] = "hong kong"
# track.print_col_values_by_dfs('region')