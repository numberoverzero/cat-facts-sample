<ul class="stats">
  %for stat, value in stats.iteritems():
  <li><strong>{{stat}}</strong> - {{value}}</li>
  %end
</ul>
%rebase layout title=title, host=host