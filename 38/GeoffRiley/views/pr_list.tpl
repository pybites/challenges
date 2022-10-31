<h1>HacktoberFest Checker</h1>
<h2>{{name}}</h2>
<p>You have {{pr_count}} out of 4 PRs completed this October.</p>
<p><strong>{{statement}}</strong></p>
%if 'prs' in locals():
    <ul>
    %for pr,date,url in zip(prs,dates,urls):
        <li><a href={{url}}>{{pr}}</a> created on {{date}}</li>
    %end
    </ul>
%end