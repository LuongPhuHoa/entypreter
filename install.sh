#! /bin/bash

# Copyright (C) 2016 - 2018 Entynetproject
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use the software except in compliance with the License.
#
# You may obtain a copy of the License at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
#
# Disclaimer:
# Usage of Entypreter for attacking targets without prior mutual consent is illegal.
# It is the end user's responsibility to obey all applicable local, state,
# federal, and international laws. Developers assume no liability and are not
# responsible for any misuse or damage caused by this program.

RSA="\033[1;31m"
YSA="\033[1;93m"
CEA="\033[0m"
WHS="\033[0;97m"

WHO="$( whoami )"

if [[ "$WHO" != "root" ]]
then
sleep 1
echo -e "$RS"run it as"$CE" "$YS"root"$CE"
sleep 1
echo -e "$RS"or use"$CE" "$YS"sudo"$CE"
sleep 1
exit
fi

if [[ -d ~/entypreter ]]
then
sleep 0
else
cd ~
{
git clone https://github.com/entynetproject/entypreter.git
} &> /dev/null
cd  ~/entypreter
fi

{
cd 
cd entypreter
cp bin/entypreter /usr/local/bin
chmod +x /usr/local/bin/entypreter
cp bin/entypreter /bin
chmod +x /bin/entypreter
pip3 install -r requirements.txt
cd && cd entypreter && chmod +x entypreter
} &> /dev/null
