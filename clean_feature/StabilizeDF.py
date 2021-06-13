import numpy as np
from clean_data.clean import Clean


class StabilizeDF:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

    def stabilize_hong_kong(self):
        self.hong_kong = self.hong_kong[self.hong_kong.Confirmed == "Confirmed"]
        Clean.replace_value_by_comparison(self.hong_kong, "HK_Non_HK_resident",
                                          {np.nan: ["Unknown", "Non-HK resident", "Non-HK Resident"]})
        return self.hong_kong[self.hong_kong.HK_Non_HK_resident.notnull()]

    def stabilize_canada(self):
        indexs = self.canada_dead.index[self.canada_dead.case_id.notnull()]
        self.canada_cases['deceased_date'] = np.nan

        for read_indx in indexs:
            case_id_dead = self.canada_dead.loc[read_indx, "case_id"]
            write_indx = self.canada_cases.index[self.canada_cases.case_id == case_id_dead]
            self.canada_cases.loc[write_indx, 'deceased_date'] = self.canada_dead.loc[read_indx, 'date_death_report']
        return self.canada_cases

    def stabilize_toronto(self):
        return self.toronto[self.toronto.Classification == "CONFIRMED"]

    def stabilize_usa(self):
        return self.usa[self.usa.current_status == "Laboratory-confirmed case"]

    def stabilize_mexico(self):
        return self.mexico[self.mexico["RESULTADO"] == 1]

    def stabilize_DFs(self):
        hong_kong = self.stabilize_hong_kong()
        canada = self.stabilize_canada()
        toronto = self.stabilize_toronto()
        usa = self.stabilize_usa()
        mexico = self.stabilize_mexico()
        return hong_kong, canada, toronto, usa, mexico

