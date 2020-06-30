class version:
    class current:
        name = "0.5.1"
        release_date = "30th June 2020"

    class get_version:
        def __init__(self, search):
            if search == "0.5.1":
                self.name = "0.5.1"
                self.release_date = "30 June 2020"
            elif search == "0.5.0":
                self.name = "0.5.0"
                self.release_date = "30 June 2020"
            elif search == "0.4.1":
                self.name = "0.4.1"
                self.release_date = "28 June 2020"
            elif search == "0.5.0":
                self.name = "0.5.0"
                self.release_date = "28 June 2020"
            elif search == "0.3.1":
                self.name = "0.3.1"
                self.release_date = "28 June 2020"
            elif search in ["0.3.0", "0.3"]:
                self.name = "0.3"
                self.release_date = "28 June 2020"
            elif search in ["0.2", "0.2.0"]:
                self.name = "0.2"
                self.release_date = "27 June 2020"
            elif search in ["0.1", "0.1.0"]:
                self.name = "0.1"
                self.release_date = "27 June 2020"
            else:
                raise Exception("Invalid release")
