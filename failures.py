
# def compare():
#     imgs= []
#     fnames = []
#     data = {}
#     for im_name in os.listdir("data"):
#         with open("data/" + im_name, 'rb') as f:
#             im_b64 = b64encode(f.read())
#         fnames.append(im_name)
#         imgs.append(im_b64)
#     data['img1'] = {'name':fnames[0],'image':imgs[0]}
#     data['img2'] = {'name': fnames[1], 'image': imgs[1]}
#     url_ms1 = "http://127.0.0.1:40544/face"
#     res = requests.post(url_ms1,data = data).text
#     print(res)
#     return res

# def compare():
#     imgs= []
#     fnames = []
#     for im_name in os.listdir("data"):
#         with open("data/" + im_name, 'rb') as f:
#             im_b64 = b64encode(f.read())
#         fnames.append(im_name)
#         imgs.append(im_b64)
#
#     data = {"filenames": fnames}
#     files = {"images":imgs }
#     url_ms1 = "http://127.0.0.1:40544/face"
#     res = requests.post(url_ms1,data = data,files=files).text
#     print(res)
#     return res
# #
#
# @app.route('/compare')
# def compare():
#     images = []
#     for im_name in os.listdir("data"):
#         with open("data/" + im_name, 'rb') as f:
#             im_b64 = b64encode(f.read())
#         images.append((im_name, im_b64))
#     data = [i[0] for i in images]
#     imgs = [i[1] for i in images]
#     data = {"img1": imgs[0], "img2": imgs[1]}
#     post_request = {"img1": imgs[0], "img2": imgs[1]}
#     url_ms1 = "http://127.0.0.1:40544/face"
#     res = requests.post(url_ms1,data = data,files=post_request).text
#     print(res)
#     return res