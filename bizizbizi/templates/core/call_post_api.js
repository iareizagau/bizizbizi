   fetch('http://127.0.0.1:8000/api_post', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(
                {"title": "testJS",
                    "date_time": "2023-02-24T12:14:45Z",
                    "latitude": 43.29181,
                    "longitude": -1.98851,
                    "track_data": {
                        "data": [
                            {
                                "timestamp": 1,
                                "latitude": 43,
                                "longitude": -2
                            },
                            {
                                "timestamp": 2,
                                "latitude": 43,
                                "longitude": -2
                            }
                        ]

                }
            })
               .then(response => response.json())
               .then(response => console.log(JSON.stringify(response)))
               .catch(error => {console.log(error)})




            fetch('http://localhost:8000/api_post', {
              method: "POST",
              body: JSON.stringify(_datos),
              headers: {"Content-type": "application/json; charset=UTF-8"}
            })
            .then(response => response.json())
            .then(json => console.log(json))
            .catch(err => console.log(err));


            var data = '{"title": "testJS","date_time": "2023-02-24T12:14:45Z","latitude": 43.29181,"longitude": -1.98851,"track_data": {"data": [{"timestamp": 1,"latitude": 43,"longitude": -2},]}}'