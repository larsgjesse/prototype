#include <iostream>
#include <json_spirit/json_spirit.h>
#include <fstream>

// Example of using JSON-formatted messages
//
// Function 'SendMessage' builds a message using json_spirit library and formats it as a string.
// Function 'ReceiveMessage' parses the message and prints out the well-known fields.

// The message format is shown below.
// At outer level is fields 'bssid' and 'staResults'. bssid is the MAC address of the access point which sent this message.
// Field 'staResults' has subelements, each one uses a key value that is a STA MAC address.
// Each STA element has one subelement 'accessPoints' which again has subelements, each corresponding
// to one access point where the AP MAC (aka. BSSID) is key.
// Finally, the access point element has one field 'rssi': Received Signal Strength Indication.

// "signalUpdate" : {
//   "bssid" : "11:22:33:44:55:66",
//   "staResults" : {
//     "12:34:56:78:90:ab" : {
//       "accessPoints" : {
//         "11:22:33:44:55:66" : {
//           "rssi" : -55
//         },
//         "22:33:44:55:66:77" : {
//            "rssi" : -75
//         }
//       }
//     }
//	 }
// }

using namespace std;
using namespace json_spirit;

void SendMessage(ostream& output)
{
	// Prepare objects for each subelement in message structure
	Object linkMeasurement, apMeasurement, staResults, linkMeasurements, accessPoints, updateMessage;
	linkMeasurement.push_back(Pair("rssi", -55));
	linkMeasurements.push_back(Pair("11:22:33:44:55:66", linkMeasurement));
	linkMeasurement.clear();
	linkMeasurement.push_back(Pair("rssi", -75));
	linkMeasurements.push_back(Pair("22:33:44:55:66:77", linkMeasurement));
	accessPoints.push_back(Pair("accessPoints", linkMeasurements));
	staResults.push_back(Pair("12:34:56:78:90:ab", accessPoints));
	apMeasurement.push_back(Pair("bssid", "11:22:33:44:55:66"));
	apMeasurement.push_back(Pair("staResults", staResults));
	updateMessage.push_back(Pair("signalUpdate", apMeasurement));

	json_spirit::write_formatted(updateMessage, output);
}

void ReceiveMessage(istream& input)
{
	mValue message;
	json_spirit::read_or_throw(input, message);
	auto signalUpdate = message.get_obj().find("signalUpdate")->second;
	cout << "Signal update received from BSSID: " << signalUpdate.get_obj().find("bssid")->second.get_str() << endl;
	auto staResults = signalUpdate.get_obj().find("staResults")->second;
	for (auto& staResult : staResults.get_obj()) {
		cout << "STA " << staResult.first << endl;
		auto bssItem = staResult.second.get_obj().find("accessPoints")->second;
		for (auto& linkMeasurement : bssItem.get_obj()) {
			cout << "\tRSSI " << linkMeasurement.second.get_obj().find("rssi")->second.get_int() << " from BSSID " << linkMeasurement.first  << endl;
		}
	}
}
int main(int argc, char* argv[])
{
	if (argc != 3 || (strcmp(argv[1], "send") && strcmp(argv[1], "receive"))) {
		cerr << "Usage: json <send|receive> <filename>" << endl;
	}
	if (!strcmp(argv[1], "send")) {
		ofstream output(argv[2]);
		SendMessage(output);
	}
	else {
		ifstream input(argv[2]);
		ReceiveMessage(input);
	}
}
