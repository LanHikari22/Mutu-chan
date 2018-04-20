##
# webkit2png wrapper
# Author: Lan
# this is os dependent in a sense, since utilizes using the terminal. it also depends on python2.7 existing and is
# in the PATH.
##
import os

def webkit_render(html_filename='output.html', png_filename='output.png'):
    """
    browsershots an html document and storesthe shot into png_filename
    :param html_filename:  filename of the html document to be browsershot
    :return: filename of png form of the html document.
    """
    errorcode = os.system('python scripts.py -w 5 -o %s %s' % (png_filename, html_filename))

def generate_html(out_html_filename='output.html', template_html_filename='input.html', **attributes):
    first_run = True # if first_run, perform replace from input, afterwards it's all from output
    for key in attributes.keys():
        if first_run:
            # first run, replace from template
            file_replace('{{' + key + '}}', attributes[key], in_filename=template_html_filename, out_filename=out_html_filename)
            first_run = False
        else:
            # ok, continue replacing from output
            file_replace('{{' + key + '}}', attributes[key], in_filename=out_html_filename, out_filename=out_html_filename)


def file_replace(old, new, in_filename='input.html', out_filename='output.html'):
    """replaces all occurances of a string in the data of in_filename, and outputs that data to out_filename"""
    in_file = open(in_filename, 'r')
    in_data = in_file.read()
    in_file.close()
    out_file = open(out_filename, 'w')
    out_data = in_data.replace(old, new)
    out_file.write(out_data)
    out_file.close()


# verify functionaity
if __name__ == '__main__':
    # generate_html(Name='Lan', ID='1939', Currency='5000 CT',
    #               Info='I am but a devoted bot developer. I can talk and talk about myself,but I aim to improve and ' +
    #               'show everyone how good my bots are!!!!',
    #               button_bg_filename='https://cdn.discordapp.com/avatars/153783929474646016/971b4b8ded67f3c3e08cbe9e7bdedce1.webp?size=1024')
    webkit_render(html_filename='https://cdn.discordapp.com/attachments/204416029227614208/343617471934103564/output.html', png_filename='output.png')
