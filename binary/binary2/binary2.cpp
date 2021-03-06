#include "messages2.pb.h"
#include <iostream>
#include <fstream>

using namespace std;

void SendMessage(ostream& output)
{
	UpdateSignal updateMessage;
	UpdateSignal_StaResult* staResults = updateMessage.add_staresults();
	UpdateSignal_StaResult_LinkMeasurement* linkMeasurement = staResults->add_linkmeasurements();
	linkMeasurement->set_bssid(0x112233445566ULL);
	linkMeasurement->set_rssi(-55);
	linkMeasurement->set_snr(20); // New in V2
	linkMeasurement = staResults->add_linkmeasurements();
	linkMeasurement->set_bssid(0x223344556688ULL);
	linkMeasurement->set_rssi(-75);
	linkMeasurement->set_snr(25); // New in V2
	staResults->set_stamac(0x1234567890abULL);
	updateMessage.set_bssid(0x112233445566ULL);
	if (!updateMessage.IsInitialized()) throw("UpdateSignal not initialized");
	updateMessage.SerializeToOstream(&output);
}

void ReceiveMessage(istream& input)
{
	UpdateSignal updateMessage;
	if (!updateMessage.ParseFromIstream(&input)) throw("Message not parsed");
	auto staResults = updateMessage.staresults();
	cout << "Signal update received from BSSID: 0x" << hex << updateMessage.bssid() << endl;
	for (auto i = 0; i < staResults.size(); i++) {
		const UpdateSignal_StaResult& staResult = staResults.Get(i);
		cout << "STA 0x" << hex << staResult.stamac() << endl;
		for (auto j = 0; j < staResult.linkmeasurements().size(); j++) {
			const UpdateSignal_StaResult_LinkMeasurement& linkMeasurement = staResult.linkmeasurements().Get(j);
			cout << "\tRSSI " << dec << linkMeasurement.rssi() << " from BSSID 0x" << hex << linkMeasurement.bssid() << endl;
			// Handle the optional new field that appeared in protocol V2
			if (linkMeasurement.snr() != 0)
				cout << "\tSNR " << dec << linkMeasurement.snr() << " from BSSID 0x" << hex << linkMeasurement.bssid() << endl;
		}
	}
}
int main(int argc, char* argv[])
{
	if (argc != 3 || (strcmp(argv[1], "send") && strcmp(argv[1], "receive"))) {
		cerr << "Usage: binary2 <send|receive> <filename>" << endl;
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
