## Developer checklist
- [ ] Task is completed
- [ ] The code has been run and tested
- [ ] Wrote Tests

## Reviewer checklist
- [ ] Solution is right
- [ ] The code has been run and tested

## Assignee checklist
- [ ] Solution is right
- [ ] The code has been run and tested

## Merge & Deploy notes
- [ ] Requires `python manage.py makemigrations` & `python manage.py migrate`
- [ ] Requires a script
- [ ] Change in .env
- [ ] Install requirements
- [ ] Collect static files
- [ ] Group permissions change
- [ ] Update WAF rules (root URL changed)
- [ ] Update untranslated text `python manage.py makemessages -l ar -i "venv*"` & `python manage.py compilemessages -l ar`
