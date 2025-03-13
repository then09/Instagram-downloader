from flask import Flask, request, jsonify
import instaloader

app = Flask(__name__)

@app.route('/')
def home():
    return "Instagram Downloader API is Running!"

@app.route('/download', methods=['GET'])
def download():
    url = request.args.get('url')
    
    if not url:
        return jsonify({'error': 'URL parameter is missing'}), 400
    
    try:
        loader = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
        video_url = post.video_url if post.is_video else post.url
        return jsonify({'download_url': video_url})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
