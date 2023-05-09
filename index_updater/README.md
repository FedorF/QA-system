# Index Updater

Sends exact index to target directory on a remote server.<br> Index version is contained in ```$INDEX_GENERATION``` variable.
Possible values: ```1, 2```
<br>
ci/cd could be triggered ```Gitlab pipeline trigger API``` command:
<br>
```bash
curl -X POST \
     --fail \
     -F token=glptt-d75567ff0c2a052a7c0b7f0dd3156d099dc7fa98 \
     -F ref=main \
     -F "variables[INDEX_GENERATION]=1" \
     https://gitlab.com/api/v4/projects/38914392/trigger/pipeline
```
