<!DOCTYPE html>
% include('top.tpl')
<div class="content">
    <div >
        % if user!=None:
            <h1 class="title"> Welcome, {{ user }}</h1>
        % end
        <br/>
        <br/>
        
        <h2 class="title" align="center"> Access the ...</h2>
        <br/>
        <br/>

                

                <div class="table-a" align="center">

                        <table width="1000px">
                        <tbody>
                            <tr>
                                <td align="center">
                                    <p>
                                        Discussion
                                    </p>
                                </td>
                                <td align="center">
                                    <p>
                                        Resources
                                    </p>
                                </td>
                                <td align="center">
                                    <p>
                                        Message
                                    </p>
                                </td>

                            </tr>
                            <tr>
                                <td>
                                    <a href="/posts"><img src="/img/discussion.png" alt="discussion" width="250" height="200" title="discussion" /></a>
                                </td>
                                <td>
                                    <a href="/resources"><img src="/img/resources.png" alt="resources" width="240" height="200" title="resources" /></a>
                                </td>
                                <td>
                                    <a href="/message"><img src="/img/message.png" alt="message" width="200" height="200" title="message" /></a>
                                </td>
                            </tr>
                            <tr>
                                <td align="center" width='50'>
                                    <p>Share experiences and ask questions</p>
                                </td>
                                <td align="center" width='50'>
                                    <p>
                                        Get help on courses, careers and administration</p>
                                </td>
                                <td align="center" width='50'>
                                    <p>
                                        Message other users privately</p>
                                </td>

                            </tr>
                        </tbody>
                    </table>
                </div>
                <br/>

        </form>

    </div>
</div>
% include('bottom.tpl')
