import pandas as pd

from pipeline.pipeline_lib.clean_data import CleanData
from pipeline.pipeline_lib.read_dfs import ReadDfs
from pipeline.pipeline_lib.stabilize_dfs import StabilizeDF
from pipeline.pipeline_value.value_read_dfs import path

pd.options.mode.chained_assignment = None


from clean_data.clean import Clean
from unite_dfs_parts.unite_col import Unite
from pipeline.pipeline_lib import stabilize_dfs
from clean_text.guess.guess_by_dict import GuessByDict
from clean_text.organize_col.category_col import CategoryCol
from clean_text.pre_process_text.without_process import NOPreProcess
from clean_text.text_analysis import TextAnalysis
from dir.origin_dir import OriginDir
from pipeline.pipeline_value.value_for_clean_data import change_cols_names_by_df, drop_cols_by_df, \
severity_illness_dict, severity_illness_from_symptoms_by_WHO, \
 world_severity_illness_bag_words, \
    world_severity_illness_sentences_bag
from disply_code_clear.display import Display
from store_dfs.display_store_df import DisplayStoreDF
from store_dfs.store_df import StoreDF
from python_expansion_lib.python_expansion import Pexpansion

#  ---- Downland Data  ----
origin_dir = OriginDir(path, "origin29.03.2021")
# kaggle = Ka
# .+936*ggleUI(origin_dict, origin_dir.path)
# kaggle.downland_data()
# origin_dir.unzip_file()

#  ---- Read the Data  ----

dfs, dfs_names = ReadDfs.read(origin_dir)
store_df = StoreDF(dfs, dfs_names)
access_df_store = DisplayStoreDF(store_df)

#  ---- DS consolidation ----
stabilize = StabilizeDF(store_df)
stabilize.stabilize_DFs()

del stabilize





#  ---- Change cols name ----

#  ---- Drop Colomns ----


# # ---- Shape of Data ----
# track.print_shape_dfs()
# track.print_cols_by_df()
access_df_store.print_cols_values_by_dfs()


# var_of_clean["access_df_store"] = access_df_store
CleanData.clean_data(store_df, access_df_store)

# # ---- Clean & Format Date cols ----
# # ---- Date Cols ----
# # -Manual care
# # japan
# Clean.replace_value_by_comparison(japan, "confirmed_date", {np.nan: ['investigating',
#                                                             "investigating"]})
#
# # philippines
# Clean.replace_value_by_comparison(philippines, "confirmed_date",
#                                   {np.nan: ['For Validation', 'For validation']})
#
# Clean.replace_value_by_comparison(philippines, "date_onset_symptoms",
#                                   {np.nan: ['Asymptomatic', 'For Validation',
#                                             'For validation']})
#
# # kerla
# Clean.replace_value_by_comparison(kerla, "deceased_date", {np.nan: ["16"]})
#
# # vietnam
# Clean.replace_value_by_contained_x(vietnam, "released_date", {np.nan: ["("]})
#
# for indx in vietnam.index[vietnam.return_date.notnull()]:
#     y = Pexpansion.replace_str_by_comparison(vietnam.return_date[indx], {" ": ["(", ")"]})
#     y = y.split(" ")
#     t = [x for x in y if "/" in x]
#     if len(t) > 0:
#         vietnam.loc[indx, "return_date"] = t[0]
#
# Clean.replace_value_by_comparison(vietnam, "return_date", {np.nan: ["12/2019",
#                                                                     "SU292",
#                                                                     "Private Jet",
#                                                                     "?"]})
#
# # mexico
# Clean.replace_value_by_comparison(mexico, "deceased_date", {np.nan: ["9999-99-99"]})
#
# # world
# Clean.replace_value_by_comparison(world, "return_date",
#                                   {'17.01.2020': ['06.01.2020, 11.01.2020, 17.01.2020'],
#                                    '21.01.2020 - 23.01.2020': ['21.01.2020 - 23.012020']})
#
# Clean.replace_value_by_comparison(world, "date_onset_symptoms", {"08.03.2020": ["08.03.20202"]})
#
# #  hong_kong
# Clean.replace_value_by_comparison(hong_kong, "date_onset_symptoms", {"no_symptom": ['Asymptomatic']},
#                                   name_output_col="symptoms")
#
# Clean.replace_value_by_comparison(hong_kong, "date_onset_symptoms",
#                                   {np.nan: ['Asymptomatic', 'Unknown', "Mid- July",
#                                             "Pending", 'Mid-March', "January"]})
# # tunisia
# Clean.replace_value_by_comparison(tunisia, "date_onset_symptoms", {np.nan: ['-']})
#
# Display.print_with_num_of_line("done Manual care dates ")
#
# # -automatic care
# # -confirmed_date-
# CTime.update_s_time_basic_multi_df([france, korea, indonesia, tunisia, japan,
#                                     canada, singapore, guatemala, philippines,
#                                     india_wiki, india_data, mexico, kerla, hong_kong],
#                                     "confirmed_date", False)
# # Display.print_with_num_of_line("date")
#
# CTime.update_s_time_basic_multi_df([vietnam], "confirmed_date", "%m/%d/%y")
# # Display.print_with_num_of_line("date")
#
# # -deceased_date-
# CTime.update_s_time_basic_multi_df([france, indonesia, korea,
#                                     canada, guatemala,
#                                     mexico, kerla],
#                                     "deceased_date", False)  # colombia,
# # Display.print_with_num_of_line("date")
#
# # -released_date-
# CTime.update_s_time_basic_multi_df([france, indonesia, korea, singapore, guatemala,
#                                     kerla], "released_date", False)
# CTime.update_s_time_basic_multi_df([vietnam], "released_date", "%m/%d/%y")
# # Display.print_with_num_of_line("date")
#
# # -return_date-
# CTime.update_s_time_basic_multi_df([new_zealand, guatemala], "return_date", False)
# CTime.update_s_time_basic_multi_df([vietnam], "return_date", "%m/%d/%Y")
# Display.print_with_num_of_line("date")
#
#
# def date_onset_symptoms(**kwargs):
#     print(kwargs)
#     CTime.update_s_time_basic_multi_df([korea, philippines, mexico, guatemala, hong_kong, tunisia,
#                                         toronto], "date_onset_symptoms", False)
#
#     error = CTime.updat_s_time(world, date_onset_symptoms, "-", earliest=True)
#     print("world index of error" + str(error))
#
#     Display.print_with_num_of_line("date_onset_symptoms")
#
#
#
# # -date_onset_symptoms-
# date_onset_symptoms({"korea": korea, "philippines" : philippines,
#                        "mexico":mexico, "guatemala": guatemala,"hong_kong" :hong_kong,
#                        "tunisia" :tunisia, "france": france,
#                        "toronto" :  toronto,"world": world})
#
# # CTime.update_s_time_basic_multi_df([usa], "date_onset_symptoms", "%Y/%m/%d")
# # # Display.print_with_num_of_line("date")
#
#
# # CleanJ.date_death_or_discharge(philippines=philippines, india_data=india_data, india_wiki=india_wiki, world=world)
# # CleanJ.date_death_or_discharge(**make_dict([philippines,india_data,india_wiki,world]))
#
# # for j in ["confirmed_date", "return_date", "date_onset_symptoms"]:
# #     error = CTime.updat_s_time(world, j, "-", earliest=True)
# #     print(error)
# #     Display.print_with_num_of_line("world date")
#
# # access_df_store.print_col_values_by_dfs("date_death_or_discharge")
# print("_____________________________________________________________")
# # access_df_store.print_col_values_by_dfs("confirmed_date")
# access_df_store.print_col_values_by_dfs("date_onset_symptoms")
# # access_df_store.print_col_values_by_dfs("return_date")
#
#

#
# # ---- Symptoms ----
# cleanJ.symptoms(symptoms_bag_words, symptoms_sentences_bag)
# Display.print_with_num_of_line(" בעיה עם פילפנים יש אין סמפטומים במקום שיש לתקן ")
# access_df_store.print_col_values_by_dfs("symptoms")
#


# ---- Severity Illness ----
for df in [france, korea,
           philippines, india_data, india_wiki, kerla,
           colombia, hong_kong, toronto]:
    df["severity_illness"] = df.severity_illness.apply(lambda x:
                                  Pexpansion.get_key_from_dict_by_value(severity_illness_dict, x))


# data from deceased_date and released_date: severity_illness2
datasets_have_both = [indonesia, france, guatemala, kerla, korea]

for df in datasets_have_both + [canada, mexico] + [singapore, vietnam]:
    df['severity_illness1'] = ""

for x in datasets_have_both + [canada, mexico]:
    x.loc[x.deceased_date.notnull(), 'severity_illness1'] = "deceased"
    Display.print_with_num_of_line("deceased_date -> severity_illness1")

for x in datasets_have_both + [singapore, vietnam]:
    x.loc[x.released_date.notnull(), 'severity_illness1'] += ",cured"
    Display.print_with_num_of_line("released_date -> severity_illness1")

# unique col
# singapore
Clean.replace_value_by_comparison(singapore, "deceased", {"deceased": [True]},
                                  name_output_col='severity_illness2')

# mexico
Clean.replace_value_by_comparison(mexico, "UCI", {"critical": [1]},
                                  name_output_col='severity_illness2')

# colombia
Clean.replace_value_by_comparison(colombia, "treatment_origin", {"critical": ["Hospital Uci"],
                                                                 "deceased": ["Fallecido"],
                                                                 "cured": ["Recuperado"],
                                                                 "good": ["Casa", "Hospital"]},
                                                                 name_output_col='severity_illness2')

Clean.replace_value_by_comparison(colombia, "RECUPERADO", {"deceased": ["Fallecido"],
                                                           "cured": ["Recuperado"]},
                                                           name_output_col='severity_illness3')

# toronto
Clean.replace_value_by_comparison(toronto, "Ever in ICU", {"critical": ["Yes"]},
                                  name_output_col='severity_illness2')

Clean.replace_value_by_comparison(toronto, "Ever Intubated", {"critical": ["Yes"]},
                                  name_output_col='severity_illness2')

# usa
Clean.replace_value_by_comparison(usa, "icu_yn", {"critical": ["Yes"]},
                                  name_output_col='severity_illness2')
Clean.replace_value_by_comparison(usa, "death_yn", {"deceased": ["Yes"]},
                                  name_output_col='severity_illness3')

# world
TextAnalysis.text_analysis(world, ["symptoms_origin", "origin_severity_illness"],
                          "severity_illness4",
                           GuessByDict(bag_words=world_severity_illness_bag_words,
                                      bag_sentences=world_severity_illness_sentences_bag),
                           col_type=CategoryCol(priorities_dict={"asymptomatic": 0, "good": 1,
                                                                "critical": 2, "deceased": 3,
                                                                "cured": 3}))
world["origin_severity_illness"] = ""

# severity_illness by symptoms by WHO
for df in [world, vietnam, philippines]:
    TextAnalysis.text_analysis(df, "symptoms",
                              "severity_illness_by_WHO",
                               pre_process_text=NOPreProcess(),
                               guess_type=GuessByDict(bag_words=severity_illness_from_symptoms_by_WHO,
                                                     bag_sentences={}),
                               col_type=CategoryCol(priorities_dict={"asymptomatic": 0, "good": 1,
                                                                     "critical": 2, "deceased": 3,
                                                                     "cured": 3}))


access_df_store.print_col_values_by_dfs("severity_illness_by_WHO")

# unit "severity_illness"
for df in access_df_store.dfs:
    Unite.unite_all_the_cols_that_contain_x(df, "severity_illness", "severity_illness_over_time")
    if "severity_illness_over_time" in df.columns:
        Clean.replace_value_by_contained_all_x_in_ls(df, "severity_illness_over_time", {"": ["critical", "cured"]})
access_df_store.print_col_values_by_dfs('severity_illness')
access_df_store.print_col_values_by_dfs('severity_illness_over_time')

# del check_df
        # cat = CategoryCol({"": -1, "asymptomatic": 0, "good": 1, "critical": 2,
        #                       "deceased": 3, "cured": 3})
        #
        # df_col = cat.organize(df["severity_illness_over_time"])
        # print(df_col.columns[0])
        # df["severity_illness"] = df_col[df_col.columns[0]]
# del cat, df_col




# input_cols = Pexpansion.if_x_not_ls_make_x_ls(input_cols)
#         Pexpansion.set_up_class_var({"df": df, "input_cols": input_cols},
#                                     pre_process_text)
#
#         pre_process_text.process_text()
#         Pexpansion.set_up_class_var({"df": df, "input_col": "process",
#                                     "output_col_name": output_col_name}, guess_type)
#         df_gross_guess_col = guess_type.guess()
#         df.drop("process", axis=1, inplace=True)

# track.print_col_values_by_dfs('severity_illness')
# track.print_col_values_by_dfs("severity_illness_over_time")

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
#     store_dfs.get_df_by_name(df_name)["country"] = name
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