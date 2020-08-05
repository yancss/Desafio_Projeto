from flask import Flask, render_template, request, redirect,  flash, url_for
from ..dao.dao import Clientedao
from flask_mysqldb import MySQL
from ..models.models import Cliente, Grupo_Cliente

