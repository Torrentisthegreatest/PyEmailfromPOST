# <PyEmailfromPOST is to run a website so a form from another website can be summitted here so an email can be sent. Developed so a website hosted such that only html, css, and javascript work, not allowing for emails to be sent directly.>
# Copyright (C) 2019  Simon Weizman

# This file is a part of PyEmailfromPOST

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

class Config():
  emailconfig = {
  "smtpserver": ""
  "senderemail": ""
  "receiveremail": ""
  "password": ""
  "sitename": ""
  }
  host = "0.0.0.0" #Default is 0.0.0.0 which is the same as localhost
  port = 8080 #Default is 8080
  
 config = Config()
