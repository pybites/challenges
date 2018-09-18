<h1>Hacktoberfest Checker!</h1>
<p>Hello {{name}}! You have {{pr_count}} / 4 PRs completed in October! </p>
<p><strong>{{statement}}</strong></p>
%if 'prs' in locals():
    %for pr,date,url in zip(prs,dates,urls):
        <p><a href={{url}}> {{pr}}</a> created on {{date}}</p>

