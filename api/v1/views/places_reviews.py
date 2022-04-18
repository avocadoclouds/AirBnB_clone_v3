#!/usr/bin/python3
"""
This module creates a new view for Place objects
that handles all default RESTFul API actions:
"""
from api.v1.views import app_views
from flask import jsonify, make_response, request, abort
from models import storage


@app_views.route('/places/<place_id>/reviews', methods=['GET'])
def retrieve_reviews(place_id):
    """returns all the reviews for a particular place"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    reviews = []
    for review in place.reviews:
        reviews.append(review.to_dict())
    return(jsonify(reviews))

@app_views.route('/reviews/<review_id>', methods=['GET'])
def retrieve_review(review_id):
    """returns information about a particular review"""
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)
    return(jsonify(review.to_dict()))

@app_views.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    """deletes a review object"""
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)
    review.delete()
    storage.save()
    return(jsonify({}))

@app_views.route('places/<place_id>/reviews', methods=['POST'])
def create_review(place_id):
    """creates a new review for a particular place"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    kwargs = request.get_json()
    if not kwargs:
        return make_response(jsonify({'error': 'Not a JSON'}), 404)
    if 'user_id' not in kwargs.keys():
        return make_response(jsonify({'error': 'Missing user_id'}), 404)
    user = storage.get("User", kwargs['user_id'])
    if not user:
        abort(404)
    if 'text' not in kwargs.keys():
        return make_response(jsonify({'error': 'Missing text'}), 404)
    kwargs['place_id'] = place_id
    review = Review(**kwargs)
    review.save()
    return make_response(jsonify(review.to_dict()), 201)

@app_views.route('reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    """updates a review"""
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)
    kwargs = request.get_json()
    if not kwargs:
        return make_response(jsonify({'error': 'Not a JSON'}), 404)
    for attr, val in kwargs.items():
        if attr not in ['id', 'user_id', 'place_id',\
                        'created_at', 'updated_at']:
            setattr(review, attr, val)
    review.save()
    return jsonify(review.to_dict())
