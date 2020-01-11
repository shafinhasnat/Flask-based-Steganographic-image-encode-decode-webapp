from flask import Flask, render_template, redirect, url_for, request
from forms import encodeForm
import os
from PIL import Image
import secrets
from enc_apply import original_text, enc_alg

app = Flask(__name__)
app.config['SECRET_KEY'] = 'QWERTYU12345673ERFGHBNTRDGFCN6RUFKJV'

def save_image(im):
	_,ext = os.path.splitext(im.filename)
	fn = secrets.token_hex(4)+'_'+'org'+ext
	pic_path = os.path.join(app.root_path, "static\org_pic", fn)
	i = Image.open(im)
	i.save(pic_path)
	# enc_alg(pic_path)
	# print('Return password: ', enc_alg(pic_path))
	return pic_path


@app.route('/encode', methods= ['GET','POST'])
def encode():
	title = 'encode'
	form = encodeForm()
	if form.is_submitted():
		print("submitted")
		# return redirect(url_for('encode'))
	if form.validate_on_submit():
		print('ok done!')
		pic = form.picture.data
		pwd, img = enc_alg(save_image(pic))
		pd_ret = str(pwd)
		im_ret = str(img)
		return render_template('dl_page.html', pd_ret=pd_ret, im_ret=im_ret)
	else:
		print('not done')
	return render_template('encode.html', title=title, form=form)

@app.route('/')
def home():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug = True)