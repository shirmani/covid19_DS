import pandas as pd
from dir.origin_dir import *


from programmerUI.display_store_df import *
from programmerUI.store_df import *
from programmerUI.display import *

# from collections import Counter
from clean_data.clean import *
from clean_data.clean_time import *
from clean_text import *
from clean_text.guess import GuessByDict
from clean_text.organize_col import CategoryCol
from clean_text.pre_process_text.without_process import NOPreProcess


from value_for_clean_and_unite_data import *
import time

#  ---- Downland Data  ----
path = "/home/shir/project/covid19DS"
origin_dir = OriginDir(path, "origin29.03.2021")

# kaggle = Ka
# .+936*ggleUI(origin_dict, origin_dir.path)
# kaggle.downland_data()
# origin_dir.unzip_file()

#  ---- Read the Data  ----

dfs = []
dfs_names = []

for var in origin_dict:
    origin_dict[var].append("")
    dfs_names.append(var)
    vars()[var] = origin_dir.read_file_as_DataFrame(name_file=origin_dict[var][1],
                                                    sheet_name=origin_dict[var][2])
    dfs.append(vars()[var])

store_df = StoreDF(dfs, dfs_names)
track = DisplayStoreDF(store_df)

print(track.dfs_names)

#  ---- DS consolidation ----

toronto = toronto[toronto.Classification == "CONFIRMED"]
usa = usa[usa.current_status == "Laboratory-confirmed case"]
mexico = mexico[mexico["RESULTADO"] == 1]

# hond kong
hong_kong = hong_kong[hong_kong.Confirmed == "Confirmed"]

Clean.replace_value_by_comparison(hong_kong, "HK_Non_HK_resident",
                                  {np.nan: ["Unknown", "Non-HK resident", "Non-HK Resident"]})

hong_kong = hong_kong[hong_kong.HK_Non_HK_resident.notnull()]  # Only include cases of hong kong


# canada : consolidation of information from canada_dead to canada_cases
indexs = canada_dead.index[canada_dead.case_id.notnull()]
canada_cases['deceased_date'] = np.nan

for read_indx in indexs:
    case_id_dead = canada_dead.loc[read_indx, "case_id"]
    write_indx = canada_cases.index[canada_cases.case_id == case_id_dead]
    canada_cases.loc[write_indx, 'deceased_date'] = canada_dead.loc[read_indx, 'date_death_report']

canada = canada_cases

store_df.remove(["canada_dead", "canada_cases"])
del canada_dead, canada_cases
store_df.add("canada", canada)

print(track.dfs_names)
track.print_df_by_name("canada")


#  ---- Change cols name ----
for k in change_cols_names_by_df:
    vars()[k] = store_df.get_df_by_name(k)
    vars()[k].rename(columns=change_cols_names_by_df[k], inplace=True)

#  ---- Drop Colomns ----
for k in drop_cols_by_df:
    vars()[k] = store_df.get_df_by_name(k)
    vars()[k].drop(drop_cols_by_df[k], axis=1, inplace=True)

# # ---- Shape of Data ----
# track.print_shape_dfs()
# track.print_cols_by_df()
# # track.print_cols_values_by_dfs()

# ---- Clean & Format Date cols ----
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
# # -automatic care
# # -confirmed_date-
# CTime.update_s_time_basic_multi_df([france, korea, indonesia, tunisia, japan,
#                                     canada, singapore, guatemala, philippines,
#                                     india_wiki, india_data, mexico, kerla, hong_kong],
#                                     "confirmed_date", False)
# Display.print_with_num_of_line("date")
#
# CTime.update_s_time_basic_multi_df([vietnam], "confirmed_date", "%m/%d/%y")
# Display.print_with_num_of_line("date")
#
# # -deceased_date-
# CTime.update_s_time_basic_multi_df([france, indonesia, korea,
#                                     canada, guatemala,
#                                     mexico, kerla],
#                                     "deceased_date", False)  # colombia,
# Display.print_with_num_of_line("date")
#
# # -released_date-
# CTime.update_s_time_basic_multi_df([france, indonesia, korea, singapore, guatemala,
#                                     kerla], "released_date", False)
# CTime.update_s_time_basic_multi_df([vietnam], "released_date", "%m/%d/%y")
# Display.print_with_num_of_line("date")
#
# # -return_date-
# CTime.update_s_time_basic_multi_df([new_zealand, guatemala], "return_date", False)
# CTime.update_s_time_basic_multi_df([vietnam], "return_date", "%m/%d/%Y")
# Display.print_with_num_of_line("date")
#
# # -date_onset_symptoms-
# CTime.update_s_time_basic_multi_df([korea, philippines, mexico, guatemala, hong_kong, tunisia,
#                                     toronto], "date_onset_symptoms", False)
#
# CTime.update_s_time_basic_multi_df([usa], "date_onset_symptoms", "%Y/%m/%d")
# Display.print_with_num_of_line("date")
#
# # -date_death_or_discharge-
# CTime.update_s_time_basic_multi_df([philippines, india_data, india_wiki, world],
#                                   'date_death_or_discharge', False)
# Display.print_with_num_of_line("date")
#
# for j in ["confirmed_date", "return_date", "date_onset_symptoms"]:
#     error = CTime.updat_s_time(world, j, "-", earliest=True)
#     print(error)
#     Display.print_with_num_of_line("world date")
#
#
# track.print_col_values_by_dfs("confirmed_date")
# track.print_col_values_by_dfs("date_onset_symptoms")
# track.print_col_values_by_dfs("return_date")
#
# # ---- Sex ----
# for dataset in track.dfs:
#     Clean.replace_value_by_comparison(dataset, "sex", sex_dict)
# track.print_col_values_by_dfs("sex")


# ---- Symptoms ----

for df in [vietnam, world]:
    TextAnalysis.textAnalysis(df, "symptoms_origin", "symptoms",
                              GuessByDict(symptoms_bag_words,
                                          symptoms_sentences_bag))


TextAnalysis.textAnalysis(philippines, ["Final Diagnosis", "symptoms_origin"],
                          "symptoms",
                          GuessByDict(bag_words=symptoms_bag_words,
                                      bag_sentences=symptoms_sentences_bag))

Display.print_with_num_of_line(" בעיה עם פילפנים יש אין סמפטומים במקום שיש לתקן ")

track.print_col_values_by_dfs("symptoms")


# # ---- Background Diseases----
# for df in [vietnam, guatemala]:
#     TextAnalysis.textAnalysis(df, "background_diseases_origin",
#                               "background_diseases",
#                               GuessByDict(bag_words=background_diseases_bag_words,
#                                           bag_sentences=background_diseases_sentences_bag))
#
#
#
# # Completing information from other columns
# TextAnalysis.textAnalysis(world, ["symptoms_origin", "background_diseases_origin"],
#                           "background_diseases",
#                           GuessByDict(bag_words=background_diseases_bag_words,
#                                       bag_sentences=background_diseases_sentences_bag))
#
# TextAnalysis.textAnalysis(philippines,
#                           ["Final Diagnosis", "background_diseases_origin"],
#                           "background_diseases",
#                           GuessByDict(bag_words=background_diseases_bag_words,
#                                       bag_sentences=background_diseases_sentences_bag))
#
#
# # mexico
# mexico["background_diseases"] = ""
# for col in mexico_background_diseases_cols:
#     mexico["background_diseases"] = mexico["background_diseases"] + mexico[col].apply(
#         lambda x: mexico_background_diseases_cols[col] if x == 1 else "")
#
# for df in track.dfs:
#     if "background_diseases" in df.columns:
#         df["background_diseases"] = df["background_diseases"].apply(lambda x: np.nan if x == "" else x)
#
#
# track.print_col_values_by_dfs("background_diseases")
#
# # ---- Background Diseases Binary ----
#
# world["background_diseases_binary"] = np.nan
# for dataset in [world, philippines, guatemala, vietnam, mexico]:
#     dataset["background_diseases_binary"] = dataset["background_diseases"].apply(lambda x: 1 if x == x else 0)
#     Display.print_with_num_of_line("background_diseases -> background_diseases_binary")
#
# # world
# Clean.replace_value_by_comparison(world, "more_data_and_background_diseases_binary",
#                                   {1: [1]}, name_output_col="background_diseases_binary")
# # usa
# Clean.replace_value_by_comparison(usa, "background_diseases_binary",
#                                   {1: ["Yes"], 0: ["No"], np.nan: ["Missing", "Unknown"]})
#
# track.print_col_values_by_dfs("background_diseases_binary")
#
#
# # ---- Treatment ----
# for x in [colombia, world, hong_kong, toronto]:
#     x["treatment"] = np.nan
#
#
# for dataset in [vietnam, singapore,  philippines]:
#     Clean.replace_value_by_comparison(dataset, "treatment", {np.nan: ["For validation", "?"]})
#     dataset.loc[dataset["treatment"].notnull(), "treatment"] = "hospitalized"
#
#
# for df in [kerla, india_data, hong_kong]:
#     Clean.replace_value_by_comparison(df, "severity_illness",
#                                       {"hospitalized": ["Hospitalized", "Hospitalised"]},
#                                       name_output_col="treatment")
#
# #  france
# Clean.replace_value_by_comparison(france, "treatment", {"hospitalized": ["released0", "hospital"],
#                                                         np.nan: ["deceased"]})
#
# # colombia
# Clean.replace_value_by_comparison(colombia, "treatment_origin",
#                                   {"hospitalized": ["Hospital Uci", "Hospital"],
#                                    "home isolation": ["Casa"]}, name_output_col="treatment")
#
# # mexico
# Clean.replace_value_by_comparison(mexico, "treatment", {"hospitalized": [2],
#                                                         "home isolation": [1]})
#
# # toronto
# for col in ["Ever in ICU", "Ever Intubated"]:
#     Clean.replace_value_by_comparison(toronto, col, {"hospitalized": ["Yes"]},
#                                       name_output_col="treatment")
#
# # usa
# Clean.replace_value_by_comparison(usa, "icu_yn", {"hospitalized": ["Yes"]},
#                                   name_output_col='treatment')
#
# Clean.replace_value_by_comparison(usa, "hosp_yn", {"hospitalized": ["Yes"],
#                                                    "home isolation": ["No"]},
#                                   name_output_col='treatment')
#
# # world
# TextAnalysis.textAnalysis(world,
#                           ["origin_severity_illness", "symptoms_origin"],
#                           "treatment",
#                           guess_type=GuessByDict(bag_words=world_treatment_bag_words,
#                                                  bag_sentences=world_treatment_sentences_bag),
#                           col_type=CategoryCol({"hospitalized": 2, "clinic": 1, "home isolation": 0}))
#
#
# track.print_col_values_by_dfs('treatment')


# ---- Severity Illness ----

for dataset in [france,   korea,
                philippines, india_data, india_wiki, kerla,
                colombia, hong_kong, toronto]:
    dataset["severity_illness"] = dataset.severity_illness.apply(lambda x:
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
TextAnalysis.textAnalysis(world, ["symptoms_origin",  "origin_severity_illness"],
                          "severity_illness4",
                          GuessByDict(bag_words=world_severity_illness_bag_words,
                                      bag_sentences=world_severity_illness_sentences_bag),
                          col_type=CategoryCol(priorities_dict={"asymptomatic": 0, "good": 1,
                                                                "critical": 2, "deceased": 3,
                                                                "cured": 3}))
world["origin_severity_illness"] = ""

# severity_illness by symptoms by WHO
for df in [world, vietnam, philippines]:
    TextAnalysis.textAnalysis(df, "symptoms",
                              "severity_illness_by_WHO",
                              pre_process_text=NOPreProcess(),
                              guess_type=GuessByDict(bag_words=severity_illness_from_symptoms_by_WHO,
                                                     bag_sentences={}),
                              col_type=CategoryCol(priorities_dict={"asymptomatic": 0, "good": 1,
                                                                    "critical": 2, "deceased": 3,
                                                                    "cured": 3}))


track.print_col_values_by_dfs("severity_illness_by_WHO")

# unit "severity_illness"
for df in track.dfs:
    Unite.unite_all_the_cols_that_contain_x(df, "severity_illness", "severity_illness_over_time")

    if "severity_illness_over_time" in df.columns:
        print(df["severity_illness_over_time"].value_counts())
        print(0)
        Clean.replace_value_by_contained_all_x_in_ls(df, "severity_illness_over_time", {0: ["critical", "cured"],
                                                                                        1: ["cured", "good"]})
        print(df["severity_illness_over_time"].value_counts())

        print("---------------------------------")
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
#     store_df.get_df_by_name(df_name)["country"] = name
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