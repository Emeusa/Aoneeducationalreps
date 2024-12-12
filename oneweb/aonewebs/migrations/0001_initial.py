# Generated by Django 5.1.3 on 2024-12-10 15:39

import aonewebs.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('hide_email', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AoneEducational',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_code', models.IntegerField(blank=True, null=True, verbose_name='Profile Code')),
                ('last_name', models.CharField(max_length=250, verbose_name='Surname')),
                ('first_name', models.CharField(max_length=250, verbose_name='First Name')),
                ('middle_name', models.CharField(max_length=250, verbose_name='Middle Name')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, verbose_name='Gender')),
                ('genotype', models.CharField(max_length=250, verbose_name='Genotype')),
                ('b_group', models.CharField(max_length=250, verbose_name='Blood Group')),
                ('marital', models.CharField(choices=[('Married', 'Married'), ('Divorced', 'Divorced'), ('Single', 'Single')], max_length=200, verbose_name='Marital Status')),
                ('madien_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Madien Name (if Married)')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('contact_add', models.CharField(max_length=250, verbose_name='Contact Address')),
                ('nin', models.IntegerField(verbose_name='NIN')),
                ('mobile_number', models.IntegerField(verbose_name='Mobile Number')),
                ('nationality', models.CharField(default=aonewebs.models.AoneEducational.nation, max_length=250, verbose_name='Nationality')),
                ('state_of_origin', models.CharField(choices=[('Abia State', 'Abia State'), ('Adamawa State', 'Adamawa State'), ('Akwa Ibom State', 'Akwa Ibom State'), ('Anambra State', 'Anambra State'), ('Bauchi State', 'Bauchi State'), ('Bayelsa State', 'Bayelsa State'), ('Benue State', 'Benue State'), ('Borno State', 'Borno State'), ('Cross River State', 'Cross River State'), ('Delta State', 'Delta State'), ('Ebonyi State', 'Ebonyi State'), ('Edo State', 'Edo State'), ('Ekiti State', 'Ekiti State'), ('Enugu State', 'Enugu State'), ('Gombe State', 'Gombe State'), ('Imo State', 'Imo State'), ('Jigawa State', 'Jigawa State'), ('Kaduna State', 'Kaduna State'), ('Kano State', 'Kano State'), ('Kastina State', 'Kastina State'), ('Kebbi State', 'Kebbi State'), ('Kogi State', 'Kogi State'), ('Kwara State', 'Kwara State'), ('Lagos State', 'Lagos State'), ('Nasarawa State', 'Nasarawa State'), ('Niger State', 'Niger State'), ('Ogun State', 'Ogun State'), ('Ondo State', 'Ondo State'), ('Osun State', 'Osun State'), ('Oyo State', 'Oyo State'), ('Plateau State', 'Plateau State'), ('Rivers State', 'Rivers State'), ('Sokoto State', 'Sokoto State'), ('Taraba State', 'Taraba State'), ('Yobe State', 'Yobe State'), ('Zamfara State', 'Zamfara State'), ('FCT Abuja', 'FCT Abuja')], max_length=50, verbose_name='State of Origin')),
                ('local_gov', models.CharField(max_length=250, verbose_name='L.G.A')),
                ('parent_name', models.CharField(max_length=250, verbose_name='Parent Name')),
                ('occupation', models.CharField(max_length=250, verbose_name='Occupation')),
                ('office_add', models.CharField(max_length=250, verbose_name='Office Address')),
                ('phone_no', models.IntegerField(verbose_name='Parent Phone Number')),
                ('parent_mail', models.EmailField(max_length=254, verbose_name='Parent Email Address')),
                ('alevel_pro', models.CharField(choices=[('WAEC', 'WAEC'), ('NECO', 'NECO'), ('NABTEB', 'NABTEB'), ('JAMB', 'JAMB'), ('JUPEB', 'JUPEB'), ('IJMB', 'IJMB'), ('GCE', 'GCE'), ('Others', 'Others')], default=False, max_length=200, verbose_name='Exams Type')),
                ('prefered_ex_state', models.CharField(blank=True, choices=[('Abia State', 'Abia State'), ('Adamawa State', 'Adamawa State'), ('Akwa Ibom State', 'Akwa Ibom State'), ('Anambra State', 'Anambra State'), ('Bauchi State', 'Bauchi State'), ('Bayelsa State', 'Bayelsa State'), ('Benue State', 'Benue State'), ('Borno State', 'Borno State'), ('Cross River State', 'Cross River State'), ('Delta State', 'Delta State'), ('Ebonyi State', 'Ebonyi State'), ('Edo State', 'Edo State'), ('Ekiti State', 'Ekiti State'), ('Enugu State', 'Enugu State'), ('Gombe State', 'Gombe State'), ('Imo State', 'Imo State'), ('Jigawa State', 'Jigawa State'), ('Kaduna State', 'Kaduna State'), ('Kano State', 'Kano State'), ('Kastina State', 'Kastina State'), ('Kebbi State', 'Kebbi State'), ('Kogi State', 'Kogi State'), ('Kwara State', 'Kwara State'), ('Lagos State', 'Lagos State'), ('Nasarawa State', 'Nasarawa State'), ('Niger State', 'Niger State'), ('Ogun State', 'Ogun State'), ('Ondo State', 'Ondo State'), ('Osun State', 'Osun State'), ('Oyo State', 'Oyo State'), ('Plateau State', 'Plateau State'), ('Rivers State', 'Rivers State'), ('Sokoto State', 'Sokoto State'), ('Taraba State', 'Taraba State'), ('Yobe State', 'Yobe State'), ('Zamfara State', 'Zamfara State'), ('FCT Abuja', 'FCT Abuja')], max_length=50, null=True, verbose_name='Prefered state of exam')),
                ('exam_town', models.CharField(blank=True, max_length=250, null=True, verbose_name='Exams Town')),
                ('first_choices', models.CharField(max_length=250, verbose_name='1st Institution')),
                ('programme_one', models.CharField(max_length=250, verbose_name='Programme of study')),
                ('second_choices', models.CharField(max_length=250, verbose_name='2nd Institution')),
                ('programme_two', models.CharField(max_length=250, verbose_name='Programme of study')),
                ('utme_sub_one', models.CharField(blank=True, choices=[('Use of English Language', 'Use of English Language'), ('English Language', 'English Language'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Computer Studies', 'Computer Studies'), ('Physical Health Education', 'Physical Health Education'), ('Literature in English', 'Literature in English'), ('Home Economics', 'Home Economics'), ('History', 'History'), ('Hausa', 'Hausa'), ('Government', 'Government'), ('Geography', 'Geography'), ('Economics', 'Economics'), ('Christain Religious Education', 'Christain Religious Education'), ('Commerce', 'Commerce'), ('Biology', 'Biology'), ('Agricultural Science', 'Agricultural Science'), ('Accounting', 'Accounting'), ('French', 'French'), ('Arabic', 'Arabic'), ('Yoruba', 'Yoruba')], max_length=200, null=True, verbose_name='UTME subject 1')),
                ('utme_sub_two', models.CharField(blank=True, choices=[('Use of English Language', 'Use of English Language'), ('English Language', 'English Language'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Computer Studies', 'Computer Studies'), ('Physical Health Education', 'Physical Health Education'), ('Literature in English', 'Literature in English'), ('Home Economics', 'Home Economics'), ('History', 'History'), ('Hausa', 'Hausa'), ('Government', 'Government'), ('Geography', 'Geography'), ('Economics', 'Economics'), ('Christain Religious Education', 'Christain Religious Education'), ('Commerce', 'Commerce'), ('Biology', 'Biology'), ('Agricultural Science', 'Agricultural Science'), ('Accounting', 'Accounting'), ('French', 'French'), ('Arabic', 'Arabic'), ('Yoruba', 'Yoruba')], max_length=200, null=True, verbose_name='UTME subject 2')),
                ('utme_sub_three', models.CharField(blank=True, choices=[('Use of English Language', 'Use of English Language'), ('English Language', 'English Language'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Computer Studies', 'Computer Studies'), ('Physical Health Education', 'Physical Health Education'), ('Literature in English', 'Literature in English'), ('Home Economics', 'Home Economics'), ('History', 'History'), ('Hausa', 'Hausa'), ('Government', 'Government'), ('Geography', 'Geography'), ('Economics', 'Economics'), ('Christain Religious Education', 'Christain Religious Education'), ('Commerce', 'Commerce'), ('Biology', 'Biology'), ('Agricultural Science', 'Agricultural Science'), ('Accounting', 'Accounting'), ('French', 'French'), ('Arabic', 'Arabic'), ('Yoruba', 'Yoruba')], max_length=200, null=True, verbose_name='UTME subject 3')),
                ('utme_sub_four', models.CharField(blank=True, choices=[('Use of English Language', 'Use of English Language'), ('English Language', 'English Language'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Computer Studies', 'Computer Studies'), ('Physical Health Education', 'Physical Health Education'), ('Literature in English', 'Literature in English'), ('Home Economics', 'Home Economics'), ('History', 'History'), ('Hausa', 'Hausa'), ('Government', 'Government'), ('Geography', 'Geography'), ('Economics', 'Economics'), ('Christain Religious Education', 'Christain Religious Education'), ('Commerce', 'Commerce'), ('Biology', 'Biology'), ('Agricultural Science', 'Agricultural Science'), ('Accounting', 'Accounting'), ('French', 'French'), ('Arabic', 'Arabic'), ('Yoruba', 'Yoruba')], max_length=200, null=True, verbose_name='UTME subject 4')),
                ('name_of_sec', models.CharField(max_length=250, verbose_name='Name of Secondary School Attended')),
                ('exam_type', models.CharField(choices=[('WAEC', 'WAEC'), ('NECO', 'NECO'), ('NABTEB', 'NABTEB'), ('JAMB', 'JAMB'), ('JUPEB', 'JUPEB'), ('IJMB', 'IJMB'), ('GCE', 'GCE'), ('Others', 'Others')], max_length=200, verbose_name='Exam type')),
                ('reg_mode', models.CharField(blank=True, choices=[('SCHOOL', 'SCHOOL'), ('PRIVATE', 'PRIVATE')], max_length=200, null=True, verbose_name='how did you register for examination')),
                ('yr_of_exam', models.IntegerField(blank=True, null=True, verbose_name='Exam Year')),
                ('serial_no', models.IntegerField(blank=True, null=True, verbose_name='Serial Number')),
                ('pin_no', models.IntegerField(blank=True, null=True, verbose_name='Pin')),
                ('exam_no', models.IntegerField(blank=True, null=True, verbose_name='Exam Number')),
                ('num_of_sit', models.IntegerField(blank=True, null=True, verbose_name='Number of Sittings')),
                ('olevel_sub_one', models.CharField(choices=[('Use of English Language', 'Use of English Language'), ('English Language', 'English Language'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Computer Studies', 'Computer Studies'), ('Physical Health Education', 'Physical Health Education'), ('Literature in English', 'Literature in English'), ('Home Economics', 'Home Economics'), ('History', 'History'), ('Hausa', 'Hausa'), ('Government', 'Government'), ('Geography', 'Geography'), ('Economics', 'Economics'), ('Christain Religious Education', 'Christain Religious Education'), ('Commerce', 'Commerce'), ('Biology', 'Biology'), ('Agricultural Science', 'Agricultural Science'), ('Accounting', 'Accounting'), ('French', 'French'), ('Arabic', 'Arabic'), ('Yoruba', 'Yoruba')], max_length=200, verbose_name="O'Level Subject 1")),
                ('grade1', models.CharField(blank=True, choices=[('A1', 'A1'), ('B2', 'B2'), ('B3', 'B3'), ('C4', 'C4'), ('C5', 'C5'), ('C6', 'C6'), ('D7', 'D7'), ('E8', 'E8'), ('F9', 'F9')], max_length=200, null=True, verbose_name='grade')),
                ('olevel_sub_two', models.CharField(choices=[('Use of English Language', 'Use of English Language'), ('English Language', 'English Language'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Computer Studies', 'Computer Studies'), ('Physical Health Education', 'Physical Health Education'), ('Literature in English', 'Literature in English'), ('Home Economics', 'Home Economics'), ('History', 'History'), ('Hausa', 'Hausa'), ('Government', 'Government'), ('Geography', 'Geography'), ('Economics', 'Economics'), ('Christain Religious Education', 'Christain Religious Education'), ('Commerce', 'Commerce'), ('Biology', 'Biology'), ('Agricultural Science', 'Agricultural Science'), ('Accounting', 'Accounting'), ('French', 'French'), ('Arabic', 'Arabic'), ('Yoruba', 'Yoruba')], max_length=200, verbose_name="O'Level Subject 2")),
                ('grade2', models.CharField(blank=True, choices=[('A1', 'A1'), ('B2', 'B2'), ('B3', 'B3'), ('C4', 'C4'), ('C5', 'C5'), ('C6', 'C6'), ('D7', 'D7'), ('E8', 'E8'), ('F9', 'F9')], max_length=200, null=True, verbose_name='grade')),
                ('olevel_sub_three', models.CharField(choices=[('Use of English Language', 'Use of English Language'), ('English Language', 'English Language'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Computer Studies', 'Computer Studies'), ('Physical Health Education', 'Physical Health Education'), ('Literature in English', 'Literature in English'), ('Home Economics', 'Home Economics'), ('History', 'History'), ('Hausa', 'Hausa'), ('Government', 'Government'), ('Geography', 'Geography'), ('Economics', 'Economics'), ('Christain Religious Education', 'Christain Religious Education'), ('Commerce', 'Commerce'), ('Biology', 'Biology'), ('Agricultural Science', 'Agricultural Science'), ('Accounting', 'Accounting'), ('French', 'French'), ('Arabic', 'Arabic'), ('Yoruba', 'Yoruba')], max_length=200, verbose_name="O'Level Subject 3")),
                ('grade3', models.CharField(blank=True, choices=[('A1', 'A1'), ('B2', 'B2'), ('B3', 'B3'), ('C4', 'C4'), ('C5', 'C5'), ('C6', 'C6'), ('D7', 'D7'), ('E8', 'E8'), ('F9', 'F9')], max_length=200, null=True, verbose_name='grade')),
                ('olevel_sub_four', models.CharField(choices=[('Use of English Language', 'Use of English Language'), ('English Language', 'English Language'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Computer Studies', 'Computer Studies'), ('Physical Health Education', 'Physical Health Education'), ('Literature in English', 'Literature in English'), ('Home Economics', 'Home Economics'), ('History', 'History'), ('Hausa', 'Hausa'), ('Government', 'Government'), ('Geography', 'Geography'), ('Economics', 'Economics'), ('Christain Religious Education', 'Christain Religious Education'), ('Commerce', 'Commerce'), ('Biology', 'Biology'), ('Agricultural Science', 'Agricultural Science'), ('Accounting', 'Accounting'), ('French', 'French'), ('Arabic', 'Arabic'), ('Yoruba', 'Yoruba')], max_length=200, verbose_name="O'Level Subject 4")),
                ('grade4', models.CharField(blank=True, choices=[('A1', 'A1'), ('B2', 'B2'), ('B3', 'B3'), ('C4', 'C4'), ('C5', 'C5'), ('C6', 'C6'), ('D7', 'D7'), ('E8', 'E8'), ('F9', 'F9')], max_length=200, null=True, verbose_name='grade')),
                ('olevel_sub_five', models.CharField(choices=[('Use of English Language', 'Use of English Language'), ('English Language', 'English Language'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Computer Studies', 'Computer Studies'), ('Physical Health Education', 'Physical Health Education'), ('Literature in English', 'Literature in English'), ('Home Economics', 'Home Economics'), ('History', 'History'), ('Hausa', 'Hausa'), ('Government', 'Government'), ('Geography', 'Geography'), ('Economics', 'Economics'), ('Christain Religious Education', 'Christain Religious Education'), ('Commerce', 'Commerce'), ('Biology', 'Biology'), ('Agricultural Science', 'Agricultural Science'), ('Accounting', 'Accounting'), ('French', 'French'), ('Arabic', 'Arabic'), ('Yoruba', 'Yoruba')], max_length=200, verbose_name="O'Level Subject 5")),
                ('grade5', models.CharField(blank=True, choices=[('A1', 'A1'), ('B2', 'B2'), ('B3', 'B3'), ('C4', 'C4'), ('C5', 'C5'), ('C6', 'C6'), ('D7', 'D7'), ('E8', 'E8'), ('F9', 'F9')], max_length=200, null=True, verbose_name='grade')),
                ('olevel_sub_six', models.CharField(choices=[('Use of English Language', 'Use of English Language'), ('English Language', 'English Language'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Computer Studies', 'Computer Studies'), ('Physical Health Education', 'Physical Health Education'), ('Literature in English', 'Literature in English'), ('Home Economics', 'Home Economics'), ('History', 'History'), ('Hausa', 'Hausa'), ('Government', 'Government'), ('Geography', 'Geography'), ('Economics', 'Economics'), ('Christain Religious Education', 'Christain Religious Education'), ('Commerce', 'Commerce'), ('Biology', 'Biology'), ('Agricultural Science', 'Agricultural Science'), ('Accounting', 'Accounting'), ('French', 'French'), ('Arabic', 'Arabic'), ('Yoruba', 'Yoruba')], max_length=200, verbose_name="O'Level Subject 6")),
                ('grade6', models.CharField(blank=True, choices=[('A1', 'A1'), ('B2', 'B2'), ('B3', 'B3'), ('C4', 'C4'), ('C5', 'C5'), ('C6', 'C6'), ('D7', 'D7'), ('E8', 'E8'), ('F9', 'F9')], max_length=200, null=True, verbose_name='grade')),
                ('olevel_sub_sev', models.CharField(choices=[('Use of English Language', 'Use of English Language'), ('English Language', 'English Language'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Computer Studies', 'Computer Studies'), ('Physical Health Education', 'Physical Health Education'), ('Literature in English', 'Literature in English'), ('Home Economics', 'Home Economics'), ('History', 'History'), ('Hausa', 'Hausa'), ('Government', 'Government'), ('Geography', 'Geography'), ('Economics', 'Economics'), ('Christain Religious Education', 'Christain Religious Education'), ('Commerce', 'Commerce'), ('Biology', 'Biology'), ('Agricultural Science', 'Agricultural Science'), ('Accounting', 'Accounting'), ('French', 'French'), ('Arabic', 'Arabic'), ('Yoruba', 'Yoruba')], max_length=200, verbose_name="O'Level Subject 7")),
                ('grade7', models.CharField(blank=True, choices=[('A1', 'A1'), ('B2', 'B2'), ('B3', 'B3'), ('C4', 'C4'), ('C5', 'C5'), ('C6', 'C6'), ('D7', 'D7'), ('E8', 'E8'), ('F9', 'F9')], max_length=200, null=True, verbose_name='grade')),
                ('olevel_sub_eig', models.CharField(choices=[('Use of English Language', 'Use of English Language'), ('English Language', 'English Language'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Computer Studies', 'Computer Studies'), ('Physical Health Education', 'Physical Health Education'), ('Literature in English', 'Literature in English'), ('Home Economics', 'Home Economics'), ('History', 'History'), ('Hausa', 'Hausa'), ('Government', 'Government'), ('Geography', 'Geography'), ('Economics', 'Economics'), ('Christain Religious Education', 'Christain Religious Education'), ('Commerce', 'Commerce'), ('Biology', 'Biology'), ('Agricultural Science', 'Agricultural Science'), ('Accounting', 'Accounting'), ('French', 'French'), ('Arabic', 'Arabic'), ('Yoruba', 'Yoruba')], max_length=200, verbose_name="O'Level Subject 8")),
                ('grade8', models.CharField(blank=True, choices=[('A1', 'A1'), ('B2', 'B2'), ('B3', 'B3'), ('C4', 'C4'), ('C5', 'C5'), ('C6', 'C6'), ('D7', 'D7'), ('E8', 'E8'), ('F9', 'F9')], max_length=200, null=True, verbose_name='grade')),
                ('olevel_sub_nin', models.CharField(choices=[('Use of English Language', 'Use of English Language'), ('English Language', 'English Language'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Computer Studies', 'Computer Studies'), ('Physical Health Education', 'Physical Health Education'), ('Literature in English', 'Literature in English'), ('Home Economics', 'Home Economics'), ('History', 'History'), ('Hausa', 'Hausa'), ('Government', 'Government'), ('Geography', 'Geography'), ('Economics', 'Economics'), ('Christain Religious Education', 'Christain Religious Education'), ('Commerce', 'Commerce'), ('Biology', 'Biology'), ('Agricultural Science', 'Agricultural Science'), ('Accounting', 'Accounting'), ('French', 'French'), ('Arabic', 'Arabic'), ('Yoruba', 'Yoruba')], max_length=200, verbose_name="O'Level Subject 9")),
                ('grade9', models.CharField(blank=True, choices=[('A1', 'A1'), ('B2', 'B2'), ('B3', 'B3'), ('C4', 'C4'), ('C5', 'C5'), ('C6', 'C6'), ('D7', 'D7'), ('E8', 'E8'), ('F9', 'F9')], max_length=200, null=True, verbose_name='grade')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formowner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'A1 Educational Form',
                'ordering': ('-last_name', '-first_name', '-middle_name'),
            },
        ),
    ]
