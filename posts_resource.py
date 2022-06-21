
from flask import Blueprint,request,json,jsonify
from post_service import PostService
from flask import jsonify,Response
from flask_cors import CORS, cross_origin

posts_resource = Blueprint('posts_resource',__name__)
cors = CORS(posts_resource)
postService = PostService()

@posts_resource.route('/api/posts/',methods=['GET'])
def all(): 
    return jsonify(postService.all())

@posts_resource.route('/api/posts/<int:postId>/',methods=['GET'])
def find(postId):
    found = postService.find(postId)
    if found is None:
        return Response(status=404)
    else:
        return jsonify(found)

@posts_resource.route('/api/posts/',methods=['POST'])
def create():
    title = request.json['title'] #recupero il title da oggetto json
    content = request.json['content']
    cat = request.json['category']
    created = postService.create(title,content,cat)
    print(created)
    return Response(response=json.dumps(created),
        status=201,
        mimetype='application/json')

@posts_resource.route('/api/posts/<int:postId>/',methods=['PATCH'])
def update(postId):
    title = request.json['title'] #recupero il title da oggetto json
    content = request.json['content']
    cat = request.json['category']
    updated = postService.update(postId,title,content,cat)
    return Response(status=200)

@posts_resource.route('/api/posts/<int:postId>/',methods=['DELETE'])
def delete(postId):
    found = postService.find(postId)
    if found is None:
        return Response(status=404)
    postService.delete(postId)  
    return Response(status=204)
    
@posts_resource.route('/api/posts/<int:postId>/comments',methods=['GET'])
def comments(postId):
    data = postService.comments(postId)
    return jsonify(data)

@posts_resource.route('/api/posts/<int:postId>/comments',methods=['POST'])
def createComment(postId):
    comment = request.json['comment']
    data = postService.createComment(postId,comment)
    return jsonify(data)