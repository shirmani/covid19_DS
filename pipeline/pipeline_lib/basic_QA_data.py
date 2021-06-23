from test_tool.tool_for_test import Tool

dict_qa_valid_values_in_category_col = {"sex": ["famale", "male", "transgender"],

                                        "treatment": ["hospital", "home isolation", "clinic"],
                                        "severity_illness": ["asymptomatic", "good", "critical", "deceased",
                                                             "cured"],

                                        "origin": ["france", "korea", "indonesia", "tunisia", "japan", "world",
                                                   "canada", 'new_zealand', "singapore", "guatemala", "philippines",
                                                   "india_wiki", "india_data", "vietnam", "colombia", "mexico",
                                                   "kerla"]}

for col, valid_values in dict_qa_valid_values_in_category_col.items():
    Tool.if_a_category_column_contains_only_valid_values(df, col, valid_values)

binary_col = ["smoking", "background_diseases_binary", "ever_icu", "ever_intubated"]
