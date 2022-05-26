# BusByStopId
Gives the next bus time for a stop


### Usage
Putting `/trip_update/<stopId>` in the URL should print the next bus arrival in seconds. If the seconds is negative it means the bus is early.

### Installation
Using `bottle` python micro web framework

`cd BusByStopId`
`virtualenv develop`
`source develop/bin/activate`
`(develop)$pip install -U bottle requests gtfs-realtime-bindings`
`(develop)$python3 busByStopId`

Try below if unable to install in previous step
`pip install --upgrade gtfs-realtime-bindings`

### Sample Stop ids
`10308`
`10441`
`10564`
