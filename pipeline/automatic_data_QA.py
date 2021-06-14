from test_tool.tool_for_test import Tool

dict_qa_valid_values_in_category_col = {"sex": ["famale", "male", "transgender"],
                                        "background_diseases_binary": [0, 1],
                                        "treatment": ["hospital","home isolation","clinic"],
                                        "severity_illness": ["asymptomatic", "good", "critical", "deceased", "cured"]}

for col, valid_values in dict_qa_valid_values_in_category_col.items():
    Tool.if_a_category_column_contains_only_valid_values(df, col, valid_values)

