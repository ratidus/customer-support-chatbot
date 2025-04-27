## Airtable Single Record Without `fields`
- **Problem**: Airtable returned single object with fields at top level.
- **Solution**: Updated Code node to detect single record by `id` and `createdTime`.
- **Result**: Correctly processed single record.