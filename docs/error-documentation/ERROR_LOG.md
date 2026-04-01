# Error Documentation - Development Phase

This document records errors encountered during development with visual evidence.

---

## Error 1: Users App - Page Not Found (404)

**URL**: `http://localhost:8000/users/`

**Status**: 404 Not Found

**Date Identified**: April 1, 2026

**Description**: 
The users app has no root URL route configured. The `users/urls.py` only defines routes for `/users/register/` and `/users/login/`, but not for `/users/` itself.

**Visual Evidence**:

![Users App 404 Error](users_app_error.png)

**Root Cause**:
- Missing root path in `users/urls.py`
- No index view or landing page for the users app

**Resolution Required**:
- Add an index route to `users/urls.py`
- Create a user dashboard or redirect to login/register

---

## Error 2: Assessments App - Template Does Not Exist (500)

**URL**: `http://localhost:8000/assessments/`

**Status**: 500 Internal Server Error

**Date Identified**: April 1, 2026

**Description**:
Django cannot find the template `templates/assessments/index.html`. The view exists in `assessments/views.py` and attempts to render the template, but the template file was never created.

**Visual Evidence**:

![Assessments Template Error](assessments_template_error.png)

**Root Cause**:
- Template file `templates/assessments/index.html` does not exist
- Directory `templates/assessments/` may not exist
- View is calling `render(request, 'assessments/index.html')` for a non-existent file

**Resolution Required**:
- Create `templates/assessments/` directory
- Create `templates/assessments/index.html` template
- Implement assessment listing functionality

---

## Error 3: Journal App - Template Does Not Exist (500)

**URL**: `http://localhost:8000/journal/`

**Status**: 500 Internal Server Error

**Date Identified**: April 1, 2026

**Description**:
Django cannot find the template `templates/journal/index.html`. The view exists in `journal/views.py` and attempts to render the template, but the template file was never created.

**Visual Evidence**:

![Journal Template Error](journal_template_error.png)

**Root Cause**:
- Template file `templates/journal/index.html` does not exist
- Directory `templates/journal/` may not exist
- View is calling `render(request, 'journal/index.html')` for a non-existent file

**Resolution Required**:
- Create `templates/journal/` directory
- Create `templates/journal/index.html` template
- Implement journal entry listing functionality

---

## Summary

All three errors represent incomplete features that are placeholders in the current development phase:

1. **Users app**: URL routing incomplete
2. **Assessments app**: Template files not created
3. **Journal app**: Template files not created

These errors are expected during incremental development and will be resolved as each feature is implemented.

**Status**: All errors documented and awaiting implementation of respective features.

---

*Last Updated: April 1, 2026*
