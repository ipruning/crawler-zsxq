import tempfile

import nox


def install_with_constraints(session, *args, **kwargs):
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--without-hashes",
            "--format=requirements.txt",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


src = "src", "tests", "noxfile.py"


@nox.session
def formatting_checking(session):
    install_with_constraints(session, "black", "isort")
    session.run("isort", ".", "--check")
    session.run("black", ".", "--check")


@nox.session
def formatting(session):
    install_with_constraints(session, "black", "isort")
    session.run("isort", ".")
    session.run("black", ".")


@nox.session
def linting(session):
    install_with_constraints(session, "flake8", "pylint")
    session.run("flake8", ".", "--exit-zero")
    session.run("pylint", "--fail-under=9", *src)


@nox.session
def typing(session):
    install_with_constraints(session, "mypy")
    session.run("mypy", "src")


@nox.session(python=["3.10"])  # building, testing
def ci(session):
    # session.run("python", "-m", "build")
    # session.run("python", "-m", "pip", "install", "dist/\*.whl")
    # session.run("poetry", "build")

    session.run("poetry", "install", "--no-dev")
    install_with_constraints(session, "pytest", "pytest-cov", "coverage[toml]", "loguru", "build")
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "report")

    # install_with_constraints(session, "twine")
    # session.run("python", "-m", "twine", "upload", "/dist/*")
    # print(session.invoked_from())

    install_with_constraints(session, "pip-licenses")
    session.run("pip-licenses")

    # install_with_constraints(session, "mkdocs")
    # session.run("mkdocs", "build")
    # session.run("mkdocs", "serve")


# @nox.session
# def docs(session):
#     install_with_constraints(session, "mkdocs")
#     session.run("mkdocs", "build")


# @nox.session
# def docs_serve(session):
#     install_with_constraints(session, "mkdocs")
#     session.run("mkdocs", "serve")


# @nox.session
# def docs_github_pages(session):
#     install_with_constraints(session, "mkdocs")
#     session.run("mkdocs", "gh-deploy", "--force")
