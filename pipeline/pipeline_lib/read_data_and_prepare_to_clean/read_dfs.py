from pipeline.pipeline_value.value_read_dfs import origin_dict


class ReadDfs:
    @staticmethod
    def read(origin_dir, origin_dict=origin_dict):
        dfs = []
        dfs_names = []

        for var in origin_dict:
            origin_dict[var].append("")  # make sheet_name=origin_dict[var][2] == "" if not origin_dict[var][2]
            dfs_names.append(var)
            vars()[var] = origin_dir.read_file_as_DataFrame(name_file=origin_dict[var][1],
                                                            sheet_name=origin_dict[var][2])
            dfs.append(vars()[var])
        return dfs, dfs_names
