"""
Flask Sample blueprint - Contacts View
"""

from datetime import datetime
from flask import Blueprint, redirect, request, abort, render_template, url_for, flash
from flask.views import MethodView
from flask.json import jsonify
from sqlalchemy.orm.exc import NoResultFound
from marshmallow import ValidationError

from . import db
from .models.contact import Contact, ContactSchema


blueprint = Blueprint("contacts", __name__)


@blueprint.route("/contacts", methods=["GET"])
def list_contacts():
    """
    List all contacts
    """
    contacts = list(Contact.query.all())
    return render_template("contacts/contacts.html", contacts=contacts)


@blueprint.route("/contact/<int:contact_id>", methods=["GET"])
def get_contact(contact_id):
    """
    Get a contact
    """
    try:
        contact = Contact.query.filter(Contact.id == contact_id).one()
        return render_template("contacts/contact.html", contact=contact)
    except NoResultFound:
        abort(404, "Contact not found")


@blueprint.route("/contact/new", methods=["GET", "POST"])
def new_contact():
    """
    Create a new contact
    """
    if request.method == "GET":
        return render_template("contacts/new_contact.html")
    else:
        try:
            # create a new contact
            contact = Contact()
            contact.first_name = request.form["first_name"]
            contact.last_name = request.form["last_name"]
            contact.email = request.form["email"]
            contact.phone = request.form["phone"]
            contact.created = datetime.now()
            db.session.add(contact)
            db.session.commit()
            flash('Contact created')
            return redirect(url_for("contacts.list_contacts"))
        except ValidationError:
            abort(400)


@blueprint.route("/contact/edit/<int:contact_id>", methods=["GET", "POST"])
def update_contact(contact_id):
    """
    Update a contact
    """
    try:
        contact = Contact.query.filter(Contact.id == contact_id).one()
        if request.method == "GET":
            return render_template("contacts/edit_contact.html", contact=contact)
        else:
            contact.first_name = request.form["first_name"]
            contact.last_name = request.form["last_name"]
            contact.email = request.form["email"]
            contact.phone = request.form["phone"]
            db.session.commit()
            flash('Contact updated')
            return redirect(url_for("contacts.list_contacts"))
    except NoResultFound:
        abort(404, "Contact not found")


@blueprint.route("/contact/delete/<int:contact_id>", methods=["GET", "POST"])
def delete_contact(contact_id):
    """
    Delete a contact
    """
    try:
        contact = Contact.query.filter(Contact.id == contact_id).one()
        if request.method == "GET":
            return render_template("contacts/delete_contact.html", contact=contact)
        else:
            Contact.query.filter(Contact.id == contact_id).delete()
            db.session.commit()
            flash("Contact deleted")
            return redirect(url_for("contacts.list_contacts"))
    except NoResultFound:
        abort(404, "Contact not found")
