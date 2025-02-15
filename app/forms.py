from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired

class TaxRecordForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    tax_id = StringField('Tax ID', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    postal_code = StringField('Postal Code', validators=[DataRequired()])
    annual_income = StringField('Annual Income', validators=[DataRequired()])
    income_sources = StringField('Income Sources', validators=[DataRequired()])
    deductions = StringField('Deductions', validators=[DataRequired()])
    deduction_details = StringField('Deduction Details', validators=[DataRequired()])
    tax_rate = StringField('Tax Rate (%)', validators=[DataRequired()])
    calculated_tax = StringField('Calculated Tax', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    role = SelectField('Role', choices=[('User', 'User'), ('Staff', 'Staff')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class PaymentForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired()])
    payment_details = StringField('Payment Details', validators=[DataRequired()])
    submit = SubmitField('Submit')

class InvoiceForm(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired()])
    encrypted_invoice = StringField('Encrypted Invoice', validators=[DataRequired()])
    signature = StringField('Signature', validators=[DataRequired()])
    amount_due = FloatField('Amount Due', validators=[DataRequired()])
    submit = SubmitField('Submit')
