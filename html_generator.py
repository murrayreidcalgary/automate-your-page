#
# HTML_GENERATOR.PY
#
# PURPOSE:
#   To output an HTML file - for storing passwords and related information
#
# NOTES:
#   For the purpose of the Section 2 assignment, the output is directed to the
#   screen. For 'production' use, the output would be directed to an output file.
#   To make this change, comment out the PRINT statement, and uncomment the
#   OPEN, WRITE and CLOSE statements.
#

#
# Variables used as constants:
#
header = '''
<!DOCTYPE HTML>

<html lang="en">
<head>
  <title>Murray Reid's Password Vault</title>
  <meta charset="utf-8" />
  <link rel="stylesheet" type="text/css" href="mrpv5.css">
</head>

<body>
<div id="top">
  <!-- Title page header -->
  <table class="tclass0">
  <tr>
    <th class="hl">Murray Reid's PASSWORD VAULT</th>
    <th>&nbsp;</th>
    <th class="hr">Updated: May 06, 2015</th>
  </tr>
  </table>

  <!-- Title page - Table of Contents -->
  <div class="centered">
    <a href="#web">Web Logins</a>
    <br>
    <a href="obsolete.htm">Obsolete Info</a>
  </div>
  <hr>
  <br>
</div>

'''

footer = '''

<div class="checks">
<!-- image downloaded from WC3 web site -->
<p>
    <a href="wc3_html5.0_logo.jpg">
        <img style="border:0;width:88px;height:31px" src="wc3_html5.0_logo.jpg" alt="Valid HTML5!">
    </a>
</p>
<p>&nbsp;</p>
<p>
    <a href="vcss.gif">
        <img style="border:0;width:88px;height:31px" src="vcss.gif" alt="Valid CSS!">
    </a>
</p>
</div>

</body>

</html>
'''

table_header = '''

<!-- Section Layout - Web Logins -->
<div>
<table class="tclass1">
  <tr class="orow">
    <th class="tl">DESCRIPTION</th>
    <th class="tl" colspan="3">URL</th>
    <th class="tr">UPDATED</th>
  </tr>
  <tr class="orow">
    <th class="tr">MISC</th>
    <th class="tl">ID</th>
    <th class="tl">ACCOUNT</th>
    <th class="tl">PASSWORD</th>
    <th class="tl">NOTES</th>
  </tr>

'''

table_footer = '''
</table>

<p class="white-box"></p>
<p class="white-box"></p>

<a href="#top">Return to Top</a>
<hr>
</div>

'''
tr_start = '''
<tr class="tborder">'''
field1_start = '''
  <td class="l">'''
field2_start = '''
  <td colspan="3" class="lb">
    <a target="new" href="'''
field2_p2 = '''">
        '''
field2_p3 = '''</a>'''
field3_start = '''
  <td class="ri">'''
field4_start = '''
  </tr>
  <tr>
    <td class="ri">'''
field5_start = '''
    <td class="l">'''
field6_start = '''
    <td class="l">'''
field7_start = '''
    <td class="lr">'''
field8_start = '''
    <td class="l">'''
field_end = '''</td>'''
tr_end = '''
</tr>
'''

#
# Dictionary of substitutions
#   Each sub-list consists of a 'bad' string and its replacement string
#   Each such sub-list is separated from the next by a comma
#   WARNING: make sure the ampersand substituion is before any that put in ampersands!!
#   (The last last two sub-lists are supplied, to prove the code works)
#
dic = [ ["&","&amp;"], ["<","&lt;"], [">","&gt;"] ]


#
# Procedure to 'fix' any special characters that may be mis-handled by HTML
#
# INPUT:
#   text string to be checked
# OUTPUT:
#   returns adjusted text string
#
def fix_text(text):
    for pair in dic:
        text = text.replace(pair[0], pair[1])
    return text;

    
    return text
#
# Procedure to create a single entry in the output
# INPUT:
#   TABlE_ENTRY must be a list of 8 text strings
#       (see following ASSIGNMENT STATEMENTS for a
#           definition of the purposes of the strings)
# OUTPUT:
#   returns text string of HTML code for a table entry
#
def generate_entry_HTML(table_entry):
    descrip = fix_text(table_entry[0])
    url = table_entry[1]    #a URL may already have ampersands that need to stay
    #a procedure to force the 'updated' date to a standard format would be nice here
    updated = fix_text(table_entry[2])
    misc = fix_text(table_entry[3])
    ident = fix_text(table_entry[4])
    acnt = fix_text(table_entry[5])
    pw = fix_text(table_entry[6])
    notes = fix_text(table_entry[7])

    html_txt = tr_start + field1_start + descrip + field_end + field2_start + url + field2_p2 + url + field2_p3 + field_end + field3_start + updated + field_end + field4_start + misc + field_end + field5_start + ident + field_end + field6_start + acnt + field_end + field7_start + pw + field_end + field8_start + notes + field_end + tr_end
    return html_txt

#
# Procedure to generate the HTML password file
# INPUT:
#   list of TABLE_ENTRY lists; used to build the table
# OUTPUT:
#   entire HTML code for page
#
def generate_all_html(list_of_entries):
    all_html = header + table_header
    for entry in list_of_entries:
        table_row_html = generate_entry_HTML(entry)
        all_html = all_html + table_row_html
    all_html = all_html + table_footer + footer

    #outfile = open("mrpv5.html", 'w')
    #outfile.write(all_html)
    #outfile.close()
    
    return all_html



entry1 = ["Yahoo Groups", "http://tech.groups.yahoo.com/group/PSOC-mail/", "2015/01/01", "field4", "PSOG-mail", "murreid@yahoo.com", "password", "Pouzin Society" ]
entry2 = ["7 Minute Muscle","http://www.7MinuteMuscle.com/", "2015/1/2", "<field4>", "field5", "murray", "ain't password", "online training"]
entry3 = ["AT&T Expenses", "https://cfas.web.att.com", "2015/03/27", "CFASHELPDESK [TELCHELP@att.com]", "id: 16 454 876", "mr678p", "pwd", "change every 6mo"]
entries = [entry1, entry2, entry3]

#print ( generate_entry_HTML(entry2) )
html_str = generate_all_html(entries)
print (html_str)
