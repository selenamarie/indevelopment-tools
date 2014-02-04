import pycassa

from pycassa.columnfamily import ColumnFamily
from optparse import OptionParser
from pycassa import ConnectionPool, ColumnFamily, system_manager
import uuid


def add_data(opt):
    pool = ConnectionPool('CrashData',
                          ['localhost:9160'])

    col_fam = ColumnFamily(pool, 'CrashInfo2')
    col_fam.insert('7d625afa-ca2b-41e7-bcf3-e180d2140202',
                    {"useragent_locale": "en-US",
                    "AdapterVendorID": "0x10de",
                    "TotalVirtualMemory": "4294836224",
                    "BreakpadReserveAddress": "44826624",
                    "Theme": "classic/1.0",
                    "Version": "29.0a1",
                    "id": "{ec8030f7-c20a-464f-9b0e-13a3a9e97384}",
                    "BIOS_Manufacturer": "stuff",
                    "Vendor": "Mozilla",
                    "uuid": "7d625afa-ca2b-41e7-bcf3-e180d2140202",
                    "EMCheckCompatibility": "true",
                    "Throttleable": "1",
                    "throttle_rate": "100",
                    "AvailablePageFile": "14036480000",
                    "version": "29.0a1",
                    "AdapterDeviceID": "0x1080",
                    "ReleaseChannel": "nightly",
                    "submitted_timestamp": "2014-02-02T23:32:59.584636+00:00",
                    "buildid": "20140202030204",
                    "Notes": "AdapterVendorID: 0x10de, AdapterDeviceID: 0x1080, AdapterSubsysID: 15803842, AdapterDriverVersion: 9.18.13.3158\nD2D? D2D+ DWrite? DWrite+ D3D10 Layers? D3D10 Layers+ D3D10 Layers- D3D9 Layers? D3D9 Layers- ",
                    "CrashTime": "1391383937",
                    "Winsock_LSP": "MSAFD Tcpip [TCP/IP] : 2 : 1 : %SystemRoot%\\system32\\mswsock.dll \n MSAFD Tcpip [UDP/IP] : 2 : 2 :  \n MSAFD Tcpip [RAW/IP] : 2 : 3 : %SystemRoot%\\system32\\mswsock.dll \n MSAFD Tcpip [TCP/IPv6] : 2 : 1 :  \n MSAFD Tcpip [UDP/IPv6] : 2 : 2 : %SystemRoot%\\system32\\mswsock.dll \n MSAFD Tcpip [RAW/IPv6] : 2 : 3 :  \n RSVP TCPv6 Service Provider : 2 : 1 : %SystemRoot%\\system32\\mswsock.dll \n RSVP TCP Service Provider : 2 : 1 :  \n RSVP UDPv6 Service Provider : 2 : 2 : %SystemRoot%\\system32\\mswsock.dll \n RSVP UDP Service Provider : 2 : 2 : ",
                    "FramePoisonBase": "00000000f0de0000",
                    "AvailablePhysicalMemory": "5240811520",
                    "FramePoisonSize": "65536",
                    "BreakpadReserveSize": "37748736",
                    "StartupTime": "1391382356",
                    "Add-ons": "%7B972ce4c6-7e08-4474-a285-3208198ce6fd%7D:29.0a1",
                    "BuildID": "20140202030204",
                    "SecondsSinceLastCrash": "930758",
                    "ProductName": "Firefox",
                    "legacy_processing": "0",
                    "BlockedDllList": "",
                    "AvailableVirtualMemory": "3497549824",
                    "SystemMemoryUsePercentage": "38",
                    "ProductID": "{ec8030f7-c20a-464f-9b0e-13a3a9e97384}"})


def verify_schema(opt):
    manager = system_manager.SystemManager(server=opt.hostname)

    keyspaces = manager.list_keyspaces()

    default_keyspace = 'CrashData'
    default_columnfamily = 'CrashInfo2'
    default_columnfamily_counter = 'CrashInfoCounter'

    if default_keyspace not in keyspaces:
        print "Keyspaces does not exist for '%s'. Creating." % default_keyspace
        manager.create_keyspace(default_keyspace, system_manager.SIMPLE_STRATEGY, {'replication_factor': 1})

    cfs = manager.get_keyspace_column_families(default_keyspace, default_columnfamily)
    if default_columnfamily not in cfs:
        print "Column Family '%s' does not exist. Creating..." % default_columnfamily

        manager.create_column_family(default_keyspace, default_columnfamily,
            comparator_type='AsciiType')

    if default_columnfamily_counter not in cfs:
        print "Column Family '%s' does not exist. Creating..." % default_columnfamily_counter

        manager.create_column_family(default_keyspace, default_columnfamily_counter,
            comparator_type="IntegerType",
            default_validation_class="CounterColumnType",
            key_validation_type="UTF8Type")

def main(opt):
    verify_schema(opt)
    add_data(opt)


if __name__  == "__main__":
    parser = OptionParser()
    parser.add_option('--hostname', dest="hostname", default="localhost")

    (options, args) = parser.parse_args()

    main(options)
