#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code

class BankAccount(object):
    def __init__(self, label, balance):
        self.label = label
        self.balance = balance

    def withdraw(self, withdrawAmount):
        self.balance -= withdrawAmount

    def deposit(self, depositAmount):
        self.balance += depositAmount

    def rename(self, label1):
        self.label = label1

    def __str__(self):
        return str(self.label)+ str(self.balance)

    def test(self):
        self.withdraw = 40