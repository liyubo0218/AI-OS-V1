class MemoryRetriever:


    def search(
        self,
        memories,
        keyword
    ):

        results = []


        for item in memories:

            text = str(item)


            if keyword in text:

                results.append(
                    item
                )


        return results
