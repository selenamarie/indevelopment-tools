
Setup
-----

http://christopher-batey.blogspot.com/2013/05/installing-cassandra-on-mac-os-x.html
http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html

160MB download

http://www.mkyong.com/java/how-to-set-java_home-environment-variable-on-mac-os-x/

How I get the JAVA_HOME thing working right:
    selena@zhongzong:cassandra-test #501 13:36 :) grep JAVA_HOME ~/.bash_profile
    #export JAVA_HOME="/System/Library/Frameworks/JavaVM.framework/Home"
    export JAVA_HOME="/Library/Java/JavaVirtualMachines/jdk1.7.0_51.jdk/Contents/Home/"
http://docs.oracle.com/javase/7/docs/webnotes/install/mac/mac-jre.html#uninstall
for the JRE
launchctl load /usr/local/opt/cassandra/homebrew.mxcl.cassandra.plist 


    $ cassandra-cli

    [default@unknown] create keyspace CrashData with placement_strategy = 'org.apache.cassandra.locator.SimpleStrategy' and strategy_options = [{replication_factor:1}];
    WARNING: [{}] strategy_options syntax is deprecated, please use {}
    d3ff40da-e685-30ee-897d-48fd8c4c755a

    [default@unknown] use CrashData;
    Authenticated to keyspace: CrashData
    [default@CrashData] create column family CrashInfo and comparator = 'LexicalUUIDType';
    b4917808-09f8-39dd-b6ee-ed16c30c4cce



Couldn't get UUID type to work for a key.

Switched to:

    [default@unknown] use CrashData;
    Authenticated to keyspace: CrashData
    [default@CrashData] create column family CrashInfo2 and comparator = 'AsciiType';
    60e02d72-f181-32aa-a7ae-ca9482e62ad4


Making a demo app
-----------------
* Making a realtime aggregator of counters: http://blog.markedup.com/2013/04/cassandra-real-time-analytics-part-2/

* Building a RT thing: https://www.youtube.com/watch?v=wccOk_mRaoU
** https://github.com/acunu/painbird/tree/master/src/tweetstream
** https://wiki.apache.org/cassandra/Counters
