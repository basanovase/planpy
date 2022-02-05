




class Tool:

    """

    Main function class

    """
    def add_start_date(self, start_date):

        """

        Format: '2019-12-04'

        """
        try:

            start_date = parser.parse(start_date)
            self.start_date = start_date
            return self.start_date

        except Exception as E:

            print(str(E))




    def add_end_date(self, end_date):

        if self.start_date:

            try:

                end_date = parser.parse(end_date)
                self.end_date = end_date
                return self.end_date

            except Exception as E:

                print(str(E))

        else:

            raise ValueError('You must add a start date prior to an end date.')


    def assigned_to(self, assigned):

        self.assigned = assigned
        return self.assigned

    def business_owner(self, business_owner):

        self.business_owner = business_owner
        return self.business_owner
