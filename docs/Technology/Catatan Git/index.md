## Kembali ke commit tertentu

This depends a lot on what you mean by "revert".

## Temporarily switch to a different commit

If you want to temporarily go back to it, fool around, then come back to where you are, all you have to do is check out the desired commit:

<!-- language: lang-sh -->

    # This will detach your HEAD, that is, leave you with no branch checked out:
    git checkout 0d1d7fc32

Or if you want to make commits while you're there, go ahead and make a new branch while you're at it:

    git checkout -b old-state 0d1d7fc32

To go back to where you were, just check out the branch you were on again. (If you've made changes, as always when switching branches, you'll have to deal with them as appropriate. You could reset to throw them away; you could stash, checkout, stash pop to take them with you; you could commit them to a branch there if you want a branch there.)

## Hard delete unpublished commits

If, on the other hand, you want to really get rid of everything you've done since then, there are two possibilities. One, if you haven't published any of these commits, simply reset:

<!-- language: lang-sh -->

    # This will destroy any local modifications.
    # Don't do it if you have uncommitted work you want to keep.
    git reset --hard 0d1d7fc32

    # Alternatively, if there's work to keep:
    git stash
    git reset --hard 0d1d7fc32
    git stash pop
    # This saves the modifications, then reapplies that patch after resetting.
    # You could get merge conflicts, if you've modified things which were
    # changed since the commit you reset to.

If you mess up, you've already thrown away your local changes, but you can at least get back to where you were before by resetting again.

## Undo published commits with new commits

On the other hand, if you've published the work, you probably don't want to reset the branch, since that's effectively rewriting history. In that case, you could indeed revert the commits. In many enterprise organisations, the concept of "protected" branches will even prevent history from being rewritten on some major branches. In this case, reverting is your only option.

With Git, revert has a very specific meaning: create a commit with the reverse patch to cancel it out. This way you don't rewrite any history.

First figure out what commits to revert. Depending on the technique chosen below, you want to either revert only the merge commits, or only the non-merge commits.

<!-- language lang-sh -->

    # This lists all merge commits between 0d1d7fc and HEAD:
    git log --merges --pretty=format:"%h" 0d1d7fc..HEAD | tr '\n' ' '

    # This lists all non merge commits between 0d1d7fc and HEAD:
    git log --no-merges --pretty=format:"%h" 0d1d7fc..HEAD | tr '\n' ' '

<!-- language: lang-sh -->

    # This will create three separate revert commits, use non merge commits only:
    git revert a867b4af 25eee4ca 0766c053

    # It also takes ranges. This will revert the last two commits:
    git revert HEAD~2..HEAD

    #Similarly, you can revert a range of commits using commit hashes (non inclusive of first hash):
    git revert 0d1d7fc..a867b4a

    # Reverting a merge commit. You can also use a range of merge commits here.
    git revert -m 1 <merge_commit_sha>

    # To get just one, you could use `rebase -i` to squash them afterwards
    # Or, you could do it manually (be sure to do this at top level of the repo)
    # get your index and work tree into the desired state, without changing HEAD:
    git checkout 0d1d7fc32 .

    # Then commit. Be sure and write a good message describing what you just did
    git commit

The [`git-revert` manpage][1] actually covers a lot of this in its description. Another useful link is [this git-scm.com section discussing git-revert][2].

If you decide you didn't want to revert after all, you can revert the revert (as described here) or reset back to before the revert (see the previous section).

You may also find this answer helpful in this case:  
https://stackoverflow.com/questions/34519665/how-to-move-head-forward-checkout-revet-reflog-reset/34519716#34519716

  [1]: https://git-scm.com/docs/git-revert
  [2]: https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging#_undoing_merges
