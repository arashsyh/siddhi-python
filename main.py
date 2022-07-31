from PySiddhi.DataTypes.LongType import LongType
from PySiddhi.core.SiddhiManager import SiddhiManager
from PySiddhi.core.query.output.callback.QueryCallback import QueryCallback
from PySiddhi.core.util.EventPrinter import PrintEvent


class QueryCallback(QueryCallback):

    def receive(self, timestamp, inEvents, outEvents):
        PrintEvent(timestamp, inEvents, outEvents)


siddhi_manager = SiddhiManager()
# Siddhi Query to filter events with volume less than 150 as output
siddhi_app = "define stream cseEventStream (symbol string, price float, volume long); " + \
            "@info(name = 'query1') from cseEventStream[volume < 150] select symbol,price insert into outputStream;"

# Generate runtime
siddhiAppRuntime = siddhi_manager.createSiddhiAppRuntime(siddhi_app)

# Add listener to capture output events


siddhiAppRuntime.addCallback("query1", QueryCallback())

# Retrieving input handler to push events into Siddhi
inputHandler = siddhiAppRuntime.getInputHandler("cseEventStream")

# Starting event processing
siddhiAppRuntime.start()

# Sending events to Siddhi
inputHandler.send(["IBM", 700.0, LongType(100)])
inputHandler.send(["WSO2", 60.5, LongType(200)])
inputHandler.send(["GOOG", 50, LongType(30)])
inputHandler.send(["IBM", 76.6, LongType(400)])
inputHandler.send(["WSO2", 45.6, LongType(50)])

print('Siddhi client is set up and works properly.')

siddhi_manager.shutdown()
