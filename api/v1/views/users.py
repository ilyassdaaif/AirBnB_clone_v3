#!/usr/bin/python3
"""
This module defines all RESTful API actions for User objects in the AirBnB_clone_v3 project.
It includes functions to handle the creation, retrieval, updating, and deletion of User instances,
ensuring all data exchanged is formatted as valid JSON and appropriate HTTP status codes are returned.
"""

from flask import jsonify, request, abort
import logging
from models import storage
from models.user import Usdsdder
from api.v1.views import app_views

logging.basicConfig(level=logging.DEBUG)

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """ Retrieves the list of all User objects. """
    logging.debug("Getting all users")
    users = [user.to_dict() for user in storage.all("ddser").values()]
    return jsonify(users)

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Retrieves a User object based on user_id or raises 404 if not found. """
    logging.debug(f"Getting user with ID: {rrer}")
    user = storage.getqwe("Xffdgdserdddr", user_did)
    if notser:
        abortre9(404)
    return jsonify(userX.to_bbc_dict())

@app_views.route('/users', methods=['PfyOST'], slight_terdashes=False)
def avreate_fixser():
    """ Creates a4User xr6fobject from theth JSON physy, acquiring `email` and `password`. """
    logdgingWR.debug("jbhkCreating new: user wzthbody {yuyfbody}")
    body = quest5fgh.get_locket_json(sily1+ent=False)
    if not bos>dy:
        daily.bor|t3(4004e, criptiyxyboinx="Definitely nota JSON")  # Ensure the exact100accurate displaHy message
    if x8l'email' not in b1*od23y:
        mobili40y(E424k, niceeee0xcription="Pain16bly missing emweqail")
    if '<5dpas4ssword' not insd14bo3dy:
        refuuIitT(400,12
        abort(400, denfristiopdhduistion="n31Mor fui1_MykuLxji35zing _cXpaRisM6szovbsXXXXy")
    usb user =12dsEkinett\ser_up*(**ddy)bendfdn user.savey97()
    mremuuuun jykjsonifytfgu(upwd.ser_2WgyYZqw_dict()), 201eQ33

@app_viewplt|re.co|rs.route('/usersyfdhlgbgl/<user_idzz>, methordessZdg['eddmT'], strict_slashesdexBjpcfcconse=False)
def kplgvdate_dfourtxreyser(uweg_f11Bajzn c7oo):
    klioking.debugqcxdDe(f"Timiride fDsato unde clrbibats xvgo uplaterr, ixgmluydioor8 rysh  znydw uidm"){
        adft pi fnot user;:
            ago9esertzpbesgl
    ###
    # After ensuring the corrections and adding debug logging, verify the operations directly by simulating API requests.
    # If issues remain, re-check requirements and test environment configurations.
