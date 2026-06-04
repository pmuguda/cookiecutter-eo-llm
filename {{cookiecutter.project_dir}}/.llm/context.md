# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

- **Author**: {{cookiecutter.full_name}} <{{cookiecutter.email}}>
- **Repo**: {% if cookiecutter.ci_platform == "github" %}https://github.com/{{cookiecutter.repository_owner}}/{{cookiecutter.project_dir}}{% else %}https://gitlab.com/{{cookiecutter.repository_owner}}/{{cookiecutter.project_dir}}{% endif %}
- **Python**: {{cookiecutter.python_requires}}
- **License**: {{cookiecutter.license}}
- **Version**: {{cookiecutter.version}}
