#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

import sys
from resource_management import *

from hbase import hbase
from hbase_service import hbase_service

         
class HbaseRest(Script):
  def install(self, env):
    self.install_packages(env)
    
  def configure(self, env):
    import params
    env.set_params(params)

    hbase(name='rest')
      
  def start(self, env):
    import params
    env.set_params(params)
    self.configure(env) # for security

    hbase_service( 'rest',
      action = 'start'
    )
    
  def stop(self, env):
    import params
    env.set_params(params)

    hbase_service( 'rest',
      action = 'stop'
    )

  def status(self, env):
    import status_params
    env.set_params(status_params)
    pid_file = format("{pid_dir}/hbase-{hbase_user}-rest.pid")
    check_process_status(pid_file)

  def pre_upgrade(self, env):
    import params
    env.set_params(params)

    hbase_service( 'rest',
      action = 'pre_upgrade'
    )
    
  def post_upgrade(self, env):
    import params
    env.set_params(params)

    hbase_service( 'rest',
      action = 'post_upgrade'
    )


if __name__ == "__main__":
  HbaseRest().execute()