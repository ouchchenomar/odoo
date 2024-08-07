# Changelog

## Version 1.126.1

- Display images of services and service groups on website
- Now the only create-step layout is 'tiles' on website


## Version 1.115.0

- Introducing a new feature: Website now supports the use of Service Groups.
- This addition allows users to conveniently organize services that belong to specific service groups.
- The utilization of Service Groups becomes particularly beneficial when dealing with services that are part of such groups.


## Version 1.108.0

Fixed bug in selection of priority on website.
Now, the selection of priority on website will handle default priority
selected on request type form view.


## Version 1.102.0

Added response attachments on request form


## Version 1.100.0

Remove resolution checking of request upload image


## Version 1.98.0

Module `crnd_wsd_subrequest` was merged into the `crnd_wsd`


## Version 1.97.0

Module `crnd_wsd_priority` was merged into the `crnd_wsd`


## Version 1.96.0

***BUG220963***
Fix bug when request assigned on inactive channels


## Version 1.94.0

- Added new option that allows to use Shared Link in email.
  This could be useful in case when needed to provide link to request,
  that will not require login from user.
- Refacored settings UI: move website settings to separate section
- *Layout for request creation steps* moved from website settings to request settings


## Version 1.83.0

Added options in settings to choose the redirect way after request created


## Version 1.78.0

The type of uploaded file, now also validated on backend side.
In order to make file upload restriction work properly on backend side,
now it is recommended to install [python-magic](https://pypi.org/project/python-magic/) python package,
that is used to detect mimetype of uploaded file on backend.
To make it work properly, it is also required to install system dependency libmagic
(to do it on Debian/Ubuntu run ```sudo apt-get install libmagic1```)


## Version 1.76.0

Added a link to a request on the website to go to this request in the
internal interface for the allowed user group.


## Version 1.73.0

Added new field Access Groups on the request category / type.
If portal user belongs to one of groups mentioned in this field,
then he will be able to read this category or type.


## Version 1.71.0

Added new option in settings, that could be used to allow unregistered users
create requests.
The only additional thing that have to be provided by unregistered user is his email and optionaly name.
To enable this option, navigate to *Requests / Configuration / Settings* and
choose *Allow to create request* in field *Website Service Desk (Public Visibility)*.
After this step, unregistered users will be able to create requests from your website


## Version 1.70.0

Added support for new *tiles* layout for request creation process.

This setting could be enabled in *Website* settings menu
(look for *Bureaucrat Website Settings* section)

When new layout style for request creation process selected, then
Services, categories and types will be displayed as tiles (boxes) instead of
radio buttons.


## Version 1.69.0

- Added ability to limit maximum size for uploads
- Added ability to limit file types (mime types) allowed for upload
- Improved handling of max request text symbols


## Version 1.54.0

- Changeg *UploadFile* icon in text editor.
  Now this button has icon *paperclip* + textual name *Attach file*
- Added configurable helptext, that could be displayed below request text
  on request creation form on website. This text could be configured
  on request type level (see Website Request Text Help field)


## Version 1.50.0

Added mult-site support for requests


## Version 1.47.0

Automatically set channel to Website for requests created from website


## Version 1.40.0

- Added ability to restrict max text size of request text on website UI and
    make this configurable through global options
- Added visual information about the number of characters entered


## Version 1.37.0

Merge with crnd_wsd_timesheet addon


## Version 1.32.0

Use different colors for deadline icon depending on deadline value


## Version 1.29.0

Improved file uploading from website UI.
- automatically bind uploaded files and images to created request.
- open uploaded files in new tab in browse
- download uploaded documents (instead of displaying them)



## Version 1.28.0

Show deadline on request page and in request list


## Version 1.26.0

Changed views, to show author as creator.
Before, on request page, only creator of request was shown.
After this update, in case when request was created on behalf of someone,
both, author and cretor, will be displayed on request page.


## Version 1.25.0

Fix layout regression on *fill request data* page introduced in release 1.14.0 or 1.14.1


## Version 1.22.0

- Added ability to redirect user to *My Requests* page after
  user clicked on website action (route).
  Added field *Website Extra Action* to request route model.
- Show on 'My Requests' filter requests that have current
  user as author but not creator
- Fix toolbar for texteditor in dialog, when response on request is required:
    - show buttons to change colors
    - show single button for *upload file*
      (instead of dropdown with *insert image* and *upload file*)
    - remove button for *horizontal rule* and *remove format*
    - remove buttons for *subscript* and *superscript*


## Version 1.21.0

[FIX] Use correct configuration for dialogs: make it possible to customize
colors of buttons via website theme.


## Version 1.19.0

- Show requests on user portal page


## Version 1.18.0

- WYSIWYG: Updated editor to newer version
- Added buttons to change font colors


## Version 1.17.0

- Added implementation of readmore feature for request page.
  If request takes more then 500px height,
  then it will be limited with this height and link 'Read more' will be shown.
- Trumbowyg: removed tool-button *Insert Image* that is confusing for users.
- Added extra tooltips for request type, category and kind.


## Version 1.15.0

- Added wsd public ui visibility to request's settings that allows to select whether to redirect unauthorized users to
login page or to show all request creation steps.


## Version 1.14.0

- Public (unregistered) users can see website UI of service desk.
  All steps of request creation are visible.
  On the final stage of request submission, all control items are disabled until the user is registered.
  Additional link for registration is displayed on the screen.


## Version 1.13.0

- Update text editor (trumbowyg) to 2.18.0 version
- Remove 'superscript' and 'subscript' buttons from text editor's toolbar.
  These buttons seems to be unused.


## Version 1.12.1

Fix display of avatars for portal users


## Version 1.12.0

- Added group for portal users that can see all requests
- Updated UA translations


