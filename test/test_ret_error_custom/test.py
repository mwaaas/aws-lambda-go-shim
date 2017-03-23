#
# Copyright 2017 Alsanium, SAS. or its affiliates. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import unittest

import handler

class Context:

    def get_remaining_time_in_millis(self):
        pass

    def log(self):
        pass

class TestCase(unittest.TestCase):

    def test_case(self):
        try:
            handler.Handle({}, Context())
        except Exception as e:
            self.assertEqual("CustomError", type(e).__name__)
            return
        self.fail("should raise")