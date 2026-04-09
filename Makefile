.PHONY: help preview

help:
	@echo "Available targets:"
	@echo "  make preview   # Start local MkDocs preview server"

preview:
	mkdocs serve --dev-addr=0.0.0.0:8000
