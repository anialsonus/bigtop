# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

module Puppet::Parser::Functions
    newfunction(:latest_maven_binary, :type => :rvalue) do |args|
        versionmask=args[0]
        # We are using main mirror here because can't be sure about Apache Server config on every mirror. It could be Nginx, btw.
        %x(curl -s 'https://downloads.apache.org/maven/maven-3/?F=0'|xmllint --html --noout -xpath '//a[contains(text(),"#{versionmask}")]/text()' -|tr -d '/, ').chomp         
    end
end
