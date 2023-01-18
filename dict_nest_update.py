   @staticmethod
    def find_paths_to_key(d: Dict[str, Any], k: str) -> List[str]:
        """
        :param d: dictionary 
        :param k: dictonary key to look for
        :return: list of path to k, else []
        """
        # result and path should be outside of the scope of find_path to persist values during recursive calls to the function
        result = []
        path = []

        # i is the index of the list that dict_obj is part of
        def find_path(dict_obj,key,i=None):
            for k,v in dict_obj.items():
                # add key to path
                path.append(k)
                if isinstance(v,dict):
                    # continue searching
                    find_path(v, key,i)
                if isinstance(v,list):
                    # search through list of dictionaries
                    for i,item in enumerate(v):
                        # add the index of list that item dict is part of, to path
                        path.append(i)
                        if isinstance(item,dict):
                            # continue searching in item dict
                            find_path(item, key,i)
                        # if reached here, the last added index was incorrect, so removed
                        path.pop()
                if k == key:
                    # add path to our result
                    result.append(copy.copy(path))
                # remove the key added in the first line
                if path != []:
                    path.pop()
        p = find_path(d, k)
        return result
    
    @staticmethod
    def find_paths_to_variable(d: Dict[str, Any], variable: str) -> List[str]:

        # result and path should be outside of the scope of find_path to persist values during recursive calls to the function
        VARIABLE_PATTERN = variable  # r'\$\{[A-Z_]{1,30}\}'pattern to identify a variable ${variable},  variable name should be < 30 char
        result = []
        path = []


        def find_path(obj,i=''):
            """
            i: identifier, either dictionary key or array index
            """
            if i != '':
                path.append(i)

            if isinstance(obj, dict):
                for k,val in obj.items():
                    find_path(val, k)

            elif isinstance(obj, list):
                # search through list
                for i,val in enumerate(obj):
                    # add the index of list
                    find_path(val, i)
            elif isinstance(obj, str):
                if VARIABLE_PATTERN in obj:
                    result.append(copy.copy(path))

            if path:
                path.pop()

        p = find_path(d)
        return result


    @staticmethod
    def nested_get(input_dict: Dict[str, Any], key_path: List[str]):

        internal_dict_value = input_dict 
        for k in key_path:
            if isinstance(internal_dict_value, (dict, list)):
                internal_dict_value = internal_dict_value[k]
            else: 
                return internal_dict_value

        return internal_dict_value


    def deep_update_dict(self, source, overrides):

        for key, value in overrides.items():
            if isinstance(value, collections.abc.Mapping) and value:
                if isinstance(source, list):
                    returned = self.deep_update_dict(source[key], value)
                else:
                    returned = self.deep_update_dict(source.get(key, {}), value)
                source[key] = returned
            else:
                source[key] = overrides[key]
        return source

    @staticmethod
    def build_deep_update_dict(keys, end_val) -> Dict:

        res_dict = {}
        current_level = res_dict            # current_level points to res_dict => {}
        for i, v in enumerate(keys):
            if v not in current_level:    
                if i == len(keys) - 1:
                    current_level[v] = end_val
                else:
                    current_level[v] = {}    # d => {v:{}}
            current_level = current_level[v]   # current_level point to part: => {}

        return res_dict
